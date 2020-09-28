import numpy as np
from ._CFunctions import _CDectoHHMM
from ._CTConv import _CTConv

def DectoHHMM(ut):
	'''
	Converts time from floating point hours with a decimal point to 
	hours, minutes, etc e.g. 19.5 -> 19:30
	
	Inputs
	======
	ut : float
		Time in hours since start of the day
		
	Returns
	=======
	hh : int32
		Hours
	mm : int32
		Minutes
	ss : int32
		Seconds
	ms : float64
		Milliseconds
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(ut),'c_int')
	_ut = _CTConv(ut,'c_double_ptr')
	_hh = np.zeros(_n,dtype='int32')
	_mm = np.zeros(_n,dtype='int32')
	_ss = np.zeros(_n,dtype='int32')
	_ms = np.zeros(_n,dtype='float64')

	#call the C++ function
	_CDectoHHMM(_n,_ut,_hh,_mm,_ss,_ms)
	
	return _hh,_mm,_ss,_ms
