from setuptools.command.install import install
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import subprocess
import os
import platform
import shutil


class CustomBuild(build_py):
	def run(self):
		self.execute(self.target_build, ())
		build_py.run(self)

	def target_build(self):
		try:
			cwd = os.getcwd()
			os.chdir('DateTimeTools/__data/datetime/')
			install_dir = f"{cwd}/DateTimeTools/__data/datetime/"
			cmd = ["cmake",f"-DCMAKE_INSTALL_PREFIX={install_dir}","-B","build"]
			subprocess.check_call(cmd, stderr=subprocess.STDOUT)
			cmd = ["cmake","--build","build"]
			subprocess.check_call(cmd, stderr=subprocess.STDOUT)
			cmd = ["cmake","--install","build"]
			subprocess.check_call(cmd, stderr=subprocess.STDOUT)

			if platform.system() == 'Windows':
				# move DLL to lib subdirectory
				old_path = f"{install_dir}/bin/libdatetime.dll"
				new_path = f"{install_dir}/lib/libdatetime.dll"
				shutil.move(old_path, new_path)
			
			os.chdir(cwd)
		except subprocess.CalledProcessError as e:
			print("Compilation failed with the following output:")
			print(e.output)
			raise			

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

setup(
	name="DateTimeTools",
	version=version,
	author="Matthew Knight James",
	author_email="mattkjames7@gmail.com",
	description="A package containing some simple tools to manage dates and times.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/mattkjames7/DateTimeTools",
	packages=find_packages(),
	package_data={"DateTimeTools.__data.datetime": ["*"]},
	cmdclass={'build_py': CustomBuild},  
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
	include_package_data=True,
)
