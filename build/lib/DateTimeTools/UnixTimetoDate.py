import numpy as np
from ._CFunctions import _CUnixTimetoDate
from ._CTConv import _CTConv

def UnixTimetoDate(unixt):
	'''
	Converts continuous time from unix time to date and time.
	
	Inputs
	======
	unixt : float64
		array of times in seconds since 19700101 at 00:00

		
	Returns
	=======
	Date : int32
		Array of dates
	ut : float32
		Array of times in hours since the start of the day
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(unixt),'c_int')
	_unixt = _CTConv(unixt,'c_double_ptr')
	_Date = np.zeros(_n,dtype='int32')
	_ut = np.zeros(_n,dtype='float32')

	#call the C++ function
	_CUnixTimetoDate(_n,_unixt,_Date,_ut)
	
	return _Date,_ut

