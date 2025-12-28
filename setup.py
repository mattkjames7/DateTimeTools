from setuptools.command.install import install
from setuptools import Extension
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import subprocess
import os
import platform
import shutil
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        super().finalize_options()
        self.root_is_pure = False

    def get_tag(self):
        # keep whatever wheel would normally do for python/abi,
        # but ensure platform is not "any"
        python, abi, plat = super().get_tag()
        return python, abi, plat


class CustomBuild(build_py):
    def run(self):
        # First build Python modules into build/lib
        super().run()

        cwd = os.getcwd()
        src_dir = os.path.join(cwd, "DateTimeTools", "__data", "datetime")
        build_dir = os.path.join(cwd, "build", "native")
        stage_dir = os.path.join(cwd, "build", "stage")

        os.makedirs(build_dir, exist_ok=True)
        os.makedirs(stage_dir, exist_ok=True)

        subprocess.check_call(
            ["cmake", "-S", src_dir, "-B", build_dir, f"-DCMAKE_INSTALL_PREFIX={stage_dir}"],
            stderr=subprocess.STDOUT,
        )
        subprocess.check_call(["cmake", "--build", build_dir], stderr=subprocess.STDOUT)
        subprocess.check_call(["cmake", "--install", build_dir], stderr=subprocess.STDOUT)

        # Find runtime libs in staging
        libs = []
        for root, _, files in os.walk(stage_dir):
            for fn in files:
                if fn.startswith("libdatetime") and (
                    fn.endswith(".so") or ".so." in fn or fn.endswith(".dylib") or fn.endswith(".dll")
                ):
                    libs.append(os.path.join(root, fn))

        if not libs:
            raise RuntimeError(f"No libdatetime found under staging dir: {stage_dir}")

        # Copy into build/lib so it goes into the wheel
        dest = os.path.join(self.build_lib, "DateTimeTools", "__data", "datetime", "lib")
        os.makedirs(dest, exist_ok=True)
        for f in libs:
            shutil.copy2(f, dest)



with open("README.md", "r") as fh:
	long_description = fh.read()

def getversion():
	'''
	read the version string from __init__
	
	'''
	#get the init file path
	thispath = os.path.abspath(os.path.dirname(__file__))+'/'
	initfile = thispath + 'DateTimeTools/__init__.py'
	
	#read the file in
	f = open(initfile,'r')
	lines = f.readlines()
	f.close()
	
	#search for the version
	version = 'unknown'
	for l in lines:
		if '__version__' in l:
			s = l.split('=')
			version = s[-1].strip().strip('"').strip("'")
			break
	return version
	
version = getversion()

if platform.system() == "Linux":
	ext_modules = [
		Extension("DateTimeTools._wheelstub", ["DateTimeTools/_wheelstub.c"],
		extra_compile_args=["-O2", "-fno-lto"],
		extra_link_args=["-Wl,--no-as-needed"],)
	]
else:
	ext_modules = [Extension("DateTimeTools._wheelstub", ["DateTimeTools/_wheelstub.c"])]


setup(
	name="DateTimeTools",
	version=version,
	author="Matthew Knight James",
	author_email="mattkjames7@gmail.com",
	description="A package containing some simple tools to manage dates and times.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/mattkjames7/DateTimeTools",
	packages=find_packages(include=["DateTimeTools*"]),
	include_package_data=False,  # IMPORTANT: don't pull MANIFEST into wheel
	package_data={
		"DateTimeTools.__data.datetime": [
			"lib/*",
		],
	},
	cmdclass={"bdist_wheel": bdist_wheel, 'build_py': CustomBuild},  
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	install_requires=[
		'numpy',
		'scipy',
		'cdflib'
	],
     ext_modules=ext_modules
)
