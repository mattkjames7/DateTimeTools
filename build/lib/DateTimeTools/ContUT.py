import numpy as np
from ._CFunctions import _CContUT
from ._CTConv import _CTConv

def ContUT(Date,ut):
	'''
	Converts date and time into continuous time - the number of hours
	since 00:00 on 1st January 1950. 
	
	Inputs
	======
	Date : int
		Array or scalar of dates
	ut : float
		Array or scalar of times in hours since the start of the day
		
	Returns
	=======
	utc : float64
		Time in hours since 19500101 at 00:00
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(ut),'c_int')
	_Date = _CTConv(Date,'c_int_ptr')
	_ut = _CTConv(ut,'c_float_ptr')
	_utc = np.zeros(_n,dtype='float64')

	#call the C++ function
	_CContUT(_n,_Date,_ut,_utc)
	
	return _utc
