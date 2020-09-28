import numpy as np
from ._CFunctions import _CWithinTimeRange
from ._CTConv import _CTConv

def WithinTimeRange(Timet,Time0,Time1,BoolOut=False):
	'''
	Performs a simple check on a test time (Timet) to see if it exists
	between Time0 and time1.
	
	Inputs
	======
	Timet : tuple | float 
		Test time - either a single floating point (array or 
		scalar) to denote hours of the day, or a tuple containing 
		(Date,Time).
	Time0 :	tuple | float
		Start time, same format as above.
	Time1 : tuple | float
		End time, same format as above.
	BoolOut : boolean
		True by default, returns a boolean array with the same size as 
		Timet, where eath element in the range Time0 to Time1 is true.
		When False, returns a list of indices within the time range.
		
	Output
	======
	out : bool | int
		If BoolOut == True boolean (array or scalar), True if within 
		time range.
		When BoolOut == False, an integer array of indices is returned.
	'''
	sh = np.shape(Timet)
	s0 = np.size(Time0)
	s1 = np.size(Time1)
	
	if s0 == 2:
		D0 = Time0[0]
		T0 = Time0[1]
	else:
		T0 = Time0
		D0 = 20000101
		
	if s1 == 2:
		D1 = Time1[0]
		T1 = Time1[1]
	else:
		T1 = Time1
		D1 = 20000101	
	
	
	if sh[0] == 2 and np.size(sh) == 2:
		#hopefully this is a list of date and time
		D = np.array([Timet[0]]).flatten()
		T = np.array([Timet[1]]).flatten()
	else: 
		T = np.array(Timet)
		D = np.zeros(T.size,dtype='int32') + 20000101
		
	#convert the dtypes for compatibility with the C++ code
	_n = _CTConv(np.size(D),'c_int')
	_Date = _CTConv(D,'c_int_ptr')
	_ut = _CTConv(T,'c_float_ptr')
	_Date0 = _CTConv(D0,'c_int')
	_ut0 = _CTConv(T0,'c_float')
	_Date1 = _CTConv(D1,'c_int')
	_ut1 = _CTConv(T1,'c_float')
	_ni = np.zeros(1,dtype='int32')
	_ind = np.zeros(_n,dtype='int32')
		
		
	#call the C++ code
	_CWithinTimeRange(_n,_Date,_ut,_Date0,_ut0,_Date1,_ut1,_ni,_ind)
	
	#reduce the side of the index array
	_ind = _ind[:_ni[0]]

	#either return the indices or the boolean array
	if BoolOut:
		out = np.zeros(_n,dtype='bool8')
		out[_ind] = True
		return out
	else:
		return _ind
