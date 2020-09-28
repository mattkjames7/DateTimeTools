import numpy as np
from ._CFunctions import _CHHMMtoDec
from ._CTConv import _CTConv

def HHMMtoDec(hh,mm=None,ss=None,ms=None):
	'''
	Converts time to floating point hours with a decimal point from
	hours, minutes, etc e.g. 19.5 -> 19:30
	
	Inputs
	======
	hh : int | float
		Hours
	mm : int | float (optional)
		Minutes
	ss : int | float (optional)
		Seconds
	ms : int | float (optional)
		Milliseconds


	Returns
	=======
	ut : float32
		Time in hours since start of the day
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(hh),'c_int')
	_hh = _CTConv(hh,'c_int_ptr')
	if not mm is None:
		_mm = _CTConv(mm,'c_int_ptr')
	else:
		_mm = np.zeros(_n,dtype='int32')
	if not ss is None:
		_ss = _CTConv(ss,'c_int_ptr')
	else:
		_ss = np.zeros(_n,dtype='int32')
	if not ms is None:
		_ms = _CTConv(ms,'c_int_ptr')
	else:
		_ms = np.zeros(_n,dtype='int32')
	_ut = np.zeros(_n,dtype='float32')

	#call the C++ function
	_CHHMMtoDec(_n,_hh,_mm,_ss,_ms,_ut)
	
	return _ut
