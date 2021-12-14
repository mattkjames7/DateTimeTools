import numpy as np
import ctypes as ct
import os
import subprocess

#Attempt to load the shared object file 
#if it can't then it probably needs recompiling
if os.name == 'nt':
	try:
		lib = ct.CDLL(os.path.dirname(__file__)+"/__data/libdatetime/libdatetime.dll")
	except:
		print('importing libdatetime.so failed, attempting to recompile')
		CWD = os.getcwd()
		os.chdir(os.path.dirname(__file__)+"/__data/libdatetime/")
		#thanks to pshustov for showing me how this is done!
		comp = subprocess.Popen('compile.bat')
		comp.communicate()
		comperr = comp.returncode
		#do something here with the error code if there is one
		
		os.chdir(CWD)
		lib = ct.CDLL(os.path.dirname(__file__)+"/__data/libdatetime/libdatetime.dll")
else:
	try:
		lib = ct.CDLL(os.path.dirname(__file__)+"/__data/libdatetime/libdatetime.so")
	except:
		print('importing libdatetime.so failed, attempting to recompile')
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
		lib = ct.CDLL(os.path.dirname(__file__)+"/__data/libdatetime/libdatetime.so")

#define some dtypes
c_char_p = ct.c_char_p
c_bool = ct.c_bool
c_int = ct.c_int
c_float = ct.c_float
c_double = ct.c_double
c_float_ptr = np.ctypeslib.ndpointer(ct.c_float,flags="C_CONTIGUOUS")
c_double_ptr = np.ctypeslib.ndpointer(ct.c_double,flags="C_CONTIGUOUS")
c_int_ptr = np.ctypeslib.ndpointer(ct.c_int,flags="C_CONTIGUOUS")
c_bool_ptr = np.ctypeslib.ndpointer(ct.c_bool,flags="C_CONTIGUOUS")

#now to define the functions

#Julian date
_CJulDay = lib.JulDay
_CJulDay.restype = None
_CJulDay.argtypes = [	c_int,			#The number of dates
						c_int_ptr,		#Array of dates
						c_float_ptr,	#Array of ut
						c_double_ptr]	#Output array of julian date
#Julian date
_CJulDaytoDate = lib.JulDaytoDate
_CJulDaytoDate.restype = None
_CJulDaytoDate.argtypes = [	c_int,		#The number of dates
						c_double_ptr,	#input julian date	
						c_int_ptr,		#Array of dates
						c_float_ptr]	#output ut

#continuous time
_CContUT = lib.ContUT
_CContUT.restype = None
_CContUT.argtypes = [	c_int,			#The number of dates
						c_int_ptr,		#Array of dates
						c_float_ptr,	#Array of ut
						c_double_ptr]	#Output array of utc
						
#Continuous time to date and time				
_CContUTtoDate = lib.ContUTtoDate
_CContUTtoDate.restype = None
_CContUTtoDate.argtypes = [	c_int,			#The number of dates
							c_double_ptr,	#Array of utc
							c_int_ptr,		#Output array of date
							c_float_ptr]	#Output array of ut
							
#unix time
_CUnixTime = lib.UnixTime
_CUnixTime.restype = None
_CUnixTime.argtypes = [	c_int,			#The number of dates
						c_int_ptr,		#Array of dates
						c_float_ptr,	#Array of ut
						c_double_ptr]	#Output array of unix time
						
#unix time to date and time				
_CUnixTimetoDate = lib.UnixTimetoDate
_CUnixTimetoDate.restype = None
_CUnixTimetoDate.argtypes = [	c_int,			#The number of dates
							c_double_ptr,	#Array of unix time
							c_int_ptr,		#Output array of date
							c_float_ptr]	#Output array of ut
							
#Date difference
_CDateDifference = lib.DateDifference
_CDateDifference.restype = c_int
_CDateDifference.argtypes = [	c_int,	#Start date
								c_int]	#End date


#Join some dates together
_CDateJoin = lib.DateJoin
_CDateJoin.restype = None
_CDateJoin.argtypes = [	c_int,		#number of elements
						c_int_ptr,	#Years
						c_int_ptr,	#Months
						c_int_ptr,	#Days
						c_int_ptr]	#Combined dates
						
#separate parts of a date integer
_CDateSplit = lib.DateSplit
_CDateSplit.restype = None
_CDateSplit.argtypes = [	c_int,		#number of elements
							c_int_ptr,	#date array
							c_int_ptr,	#years
							c_int_ptr,	#months
							c_int_ptr]	#days

#calculate day number
_CDayNo = lib.DayNo
_CDayNo.restype = None
_CDayNo.argtypes = [	c_int,		#number of elements
						c_int_ptr,	#date array
						c_int_ptr,	#output years
						c_int_ptr]	#output day numbers
						
#convert year and day number back to date
_CDayNotoDate = lib.DayNotoDate
_CDayNotoDate.restype = None
_CDayNotoDate.argtypes = [	c_int,		#number of elements
							c_int_ptr,	#years
							c_int_ptr,	#day numbers
							c_int_ptr]	#dates
							

#converting times
_CDectoHHMM = lib.DectoHHMM
_CDectoHHMM.restype = None
_CDectoHHMM.argtypes = [	c_int,			#number of elements
							c_double_ptr,	#input ut
							c_int_ptr,		#hours
							c_int_ptr,		#miinutes,
							c_int_ptr,		#seconds
							c_double_ptr]	#milliseconds	

_CHHMMtoDec = lib.HHMMtoDec
_CHHMMtoDec.restype = None
_CHHMMtoDec.argtypes = [	c_int,			#number of elements
							c_double_ptr,	#hours
							c_double_ptr,	#minutes
							c_double_ptr,	#seconds
							c_double_ptr,	#milliseconds
							c_double_ptr]	#output ut	

#find out if a year is a leap year or not
_CLeapYear = lib.LeapYear
_CLeapYear.restype = None
_CLeapYear.argtypes = [	c_int,			#number of elements
						c_int_ptr,		#years
						c_bool_ptr]		#output boolean array
						
#find the middle time 
_CMidTime = lib.MidTime
_CMidTime.restype = None
_CMidTime.argtypes = [	c_int,		#start date
						c_float,	#start time
						c_int,		#end date
						c_float,	#end time
						c_int_ptr,	#output middle date
						c_float_ptr]#output middle ut
						
#minus day
_CMinusDay = lib.MinusDay
_CMinusDay.restype = c_int		#output date
_CMinusDay.argtypes = [	c_int]	#input date

#find the nearest time index
_CNearestTimeIndex = lib.NearestTimeIndex
_CNearestTimeIndex.restype = c_int #index of input array which is closest to test time
_CNearestTimeIndex.argtypes = [	c_int,			#number of elements
								c_int_ptr,		#dates
								c_float_ptr,	#ut
								c_int,			#test date
								c_float]		#test ut
	
#plus day
_CPlusDay = lib.PlusDay
_CPlusDay.restype = c_int		#output date
_CPlusDay.argtypes = [	c_int]	#input date

#TimeDifference
_CTimeDifference = lib.TimeDifference
_CTimeDifference.restype = c_float
_CTimeDifference.argtypes = [	c_int,	#start date
								c_float,#start time
								c_int,	#end date
								c_float]#end time
								
#find the elements which are within a time range
_CWithinTimeRange = lib.WithinTimeRange
_CWithinTimeRange.restype = None
_CWithinTimeRange.argtypes = [	c_int,		#number of elements
								c_int_ptr,	#dates
								c_float_ptr,#times
								c_int,		#start date
								c_float,	#start time
								c_int,		#end date
								c_float,	#end time
								c_int_ptr,	#number of indices
								c_int_ptr]	#index array
								
							
