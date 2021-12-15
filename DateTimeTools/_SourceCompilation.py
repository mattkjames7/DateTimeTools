import os
import subprocess

def compileSource():
	"""Runs a script to compile the source files."""
	if os.name == 'nt':
		#code specifically for Windows
		CWD = os.getcwd()
		os.chdir(os.path.dirname(__file__) + os.path.sep + "__data" + os.path.sep + "libdatetime")
		compile = subprocess.Popen("compile.bat")
		compile.communicate()
		comperr = compile.returncode
		if comperr == 6:
			exstr = 'Cannot compile libdatetime: g++ not found\nPlease install TDM-GCC'
			raise Exception(exstr)
		if comperr == 7:
			exstr = 'Compilation failed\n'
			exstr+= 'Please check your g++ configuration and consider opening an issue at\n'
			exstr+= 'https://github.com/mattkjames7/DateTimeTools/issues'
			raise Exception(exstr)
		os.chdir(CWD)
	else:
		#Assume that this will work on both Linux and Mac
		#check if we need root or not!
		path = os.path.dirname(__file__)
		if '/usr/local/' in path:
			sudo = 'sudo '
		else:
			sudo = ''

		CWD = os.getcwd()
		os.chdir(os.path.dirname(__file__)+"/__data/libdatetime/")
		os.system(sudo+'make clean')
		os.system(sudo+'make')
		os.chdir(CWD)	


def getLibFilename(isShort=False):
	"""
	Return library filename string
	
	Inputs
	======
	isShort : bool 
		If False return filename with full path, if True return only filename
		default - False
	
	Returns
	=======
	libFilename	: str
		Filename of the CONFLICT (content): Merge conflict in DateTimeTools/_CFunctions.py
source library
	
	"""
	if(isShort):
		libFilename = "libdatetime."
	else:
		vv = os.path.sep
		libFilename = os.path.dirname(__file__) + vv + "__data" + vv + "libdatetime" + vv + "libdatetime."


	if(os.name=='nt'):
		extention = "dll"
	else:
		extention = "so"
	
	return libFilename + extention


def checkLibExists():
	"""Check if library file exist, and start compilation script if not."""
	if not os.path.isfile(getLibFilename()):
		print(getLibFilename(isShort=True)+" not found - attempting compilation!")
		compileSource()
