from setuptools.command.install import install
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import subprocess
import os
import platform


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
				
				# Copy the built library to the lib directory where Python expects it
				import shutil
				lib_dir = os.path.join(os.getcwd(), 'lib')
				os.makedirs(lib_dir, exist_ok=True)
				
				# Determine library extension based on platform
				if platform.system() == 'Linux':
					lib_ext = 'so'
				elif platform.system() == 'Darwin':
					lib_ext = 'dylib'
				else:
					lib_ext = 'so'
				
				# Find and copy the library from the build directory
				lib_name = f'libdatetime.{lib_ext}'
				src_lib = os.path.join('build', lib_name)
				if os.path.isfile(src_lib):
					dst_lib = os.path.join(lib_dir, lib_name)
					shutil.copy2(src_lib, dst_lib)
					print(f"Copied {src_lib} to {dst_lib}")
				else:
					# Try to find in src subdirectory
					src_lib = os.path.join('build', 'src', lib_name)
					if os.path.isfile(src_lib):
						dst_lib = os.path.join(lib_dir, lib_name)
						shutil.copy2(src_lib, dst_lib)
						print(f"Copied {src_lib} to {dst_lib}")
					else:
						print(f"Warning: Could not find {lib_name} in build directory")
				
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
	package_data={'DateTimeTools': ['__data/datetime/**/*']},
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
