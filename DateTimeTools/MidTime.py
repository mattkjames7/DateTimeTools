import numpy as np
from ._CFunctions import _CMidTime
from ._CTConv import _CTConv


def MidTime(Date0,ut0,Date1,ut1):
	'''
	Calculate the midpoint in time between two dates and times.
	
	Inputs
	======
	Date0 : int
		Start date with format YYYYMMSS.
	ut0 : float
		Start time, floating point hours.
	Date1 : int
		End date with format YYYYMMSS.
	ut1 : float
		End time in floating point hours.
		
	Returns
	=======
	mDate : int32
		Date at mid point.
	mut : float32
		Floating point time at midpoint.
	'''
	
	#convert the data types
	_Date0 = _CTConv(Date0,'c_int')
	_ut0 = _CTConv(ut0,'c_float')
	_Date1 = _CTConv(Date1,'c_int')
	_ut1 = _CTConv(ut1,'c_float')
	_mDate = np.zeros(1,dtype='int32')
	_mut = np.zeros(1,dtype='float32')

	#run the C++ routine
	_CMidTime(_Date0,_ut0,_Date1,_ut1,_mDate,_mut)
	
	return _mDate,_mut
