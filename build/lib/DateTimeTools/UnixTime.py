import numpy as np
from ._CFunctions import _CUnixTime
from ._CTConv import _CTConv

def UnixTime(Date,ut):
	'''
	Converts date and time into unix time - the number of seconds
	since 00:00 on 1st January 1970. 
	
	Inputs
	======
	Date : int
		Array or scalar of dates
	ut : float
		Array or scalar of times in hours since the start of the day
		
	Returns
	=======
	utc : float64
		Time in seconds since 19700101 at 00:00
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(ut),'c_int')
	_Date = _CTConv(Date,'c_int_ptr')
	_ut = _CTConv(ut,'c_float_ptr')
	_unixt = np.zeros(_n,dtype='float64')

	#call the C++ function
	_CUnixTime(_n,_Date,_ut,_unixt)
	
	return _unixt
