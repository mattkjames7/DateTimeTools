import numpy as np
from ._CFunctions import _CContUTtoDate
from ._CTConv import _CTConv

def ContUTtoDate(utc):
	'''
	Converts continuous time fron ContUT to date and time.
	
	Inputs
	======
	utc : float64
		array of times in hours since 19500101 at 00:00

		
	Returns
	=======
	Date : int32
		Array of dates
	ut : float32
		Array of times in hours since the start of the day
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(utc),'c_int')
	_utc = _CTConv(utc,'c_double_ptr')
	_Date = np.zeros(_n,dtype='int32')
	_ut = np.zeros(_n,dtype='float32')

	#call the C++ function
	_CContUTtoDate(_n,_utc,_Date,_ut)
	
	return _Date,_ut

