from setuptools.command.install import install
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import subprocess
import os
import platform
from getversion import getversion


class CustomBuild(build_py):
	def run(self):
		self.execute(self.target_build, ())
		build_py.run(self)

	def target_build(self):
		try:
			if platform.system() == 'Windows':
				cwd = os.getcwd()
				os.chdir('DateTimeTools/__data/datetime/')
				cmd = ['cmd','/c','compile.bat']
				subprocess.check_call(cmd, stderr=subprocess.STDOUT)
				os.chdir(cwd)
			else:
				#cmd = ['make', '-C', 'DateTimeTools/__data/datetime']
				cwd = os.getcwd()
				os.chdir('DateTimeTools/__data/datetime/')
				cmd = ["cmake","-DCMAKE_INSTALL_PREFIX=/usr/local","-B","build"]
				subprocess.check_call(cmd, stderr=subprocess.STDOUT)
				cmd = ["cmake","--build","build"]
				subprocess.check_call(cmd, stderr=subprocess.STDOUT)
				os.chdir(cwd)
		except subprocess.CalledProcessError as e:
			print("Compilation failed with the following output:")
			print(e.output)
			raise			

with open("README.md", "r") as fh:
	long_description = fh.read()

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
	package_data={'datetime': ['**/*']},
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
