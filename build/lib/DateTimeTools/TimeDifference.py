import numpy as np
from ._CFunctions import _CTimeDifference
from ._CTConv import _CTConv


def TimeDifference(Date0,ut0,Date1,ut1):
	'''
	Calculates the time difference between two dates and times.
	
	Inputs
	======
	Date0 : int
		Start date, format YYYYMMDD.
	ut0 : float
		Floating point start time in hours.
	Date1 : int
		End date, format YYYYMMDD.
	ut1 : float
		End time, floating point hours.
		
	Returns
	=======
	tdiff : float32
		Time difference in days (floating point), where positive values 
		imply that D0,T0 is before D1,T1.
	'''
	#convert the data types
	_Date0 = _CTConv(Date0,'c_int')
	_ut0 = _CTConv(ut0,'c_float')
	_Date1 = _CTConv(Date1,'c_int')
	_ut1 = _CTConv(ut1,'c_float')


	#run the C++ routine
	return _CTimeDifference(_Date0,_ut0,_Date1,_ut1)
	

