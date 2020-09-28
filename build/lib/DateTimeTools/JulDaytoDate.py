import numpy as np
from ._CFunctions import _CJulDaytoDate
from ._CTConv import _CTConv

def JulDaytoDate(jd):
	'''
	Converts Julian date to date and time.
	
	Inputs
	======
	jd : float64
		julian date

		
	Returns
	=======
	Date : int32
		Array of dates
	ut : float32
		Array of times in hours since the start of the day
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(jd),'c_int')
	_jd = _CTConv(jd,'c_double_ptr')
	_Date = np.zeros(_n,dtype='int32')
	_ut = np.zeros(_n,dtype='float32')

	#call the C++ function
	_CJulDaytoDate(_n,_jd,_Date,_ut)
	
	return _Date,_ut

