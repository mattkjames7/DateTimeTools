import numpy as np
from ._CFunctions import _CNearestTimeIndex
from ._CTConv import _CTConv

def NearestTimeIndex(Date,ut,tDate,tut):
	'''
	Finds the array index of the closest point in time, within a series 
	of dates and times.
	
	Inputs
	======
	Date : int
		Date array.
	ut : float
		Time Array.
	tDate : int
		test date.
	tut : float
		test time.
		
	Returns
	=======
	ind : int32
		Integer index of closest date/time (D,T) to the test date/time
		(Dt,Tt).
	'''
	
	#convert the data types
	_n = _CTConv(np.size(ut),'c_int')
	_Date = _CTConv(Date,'c_int_ptr')
	_ut = _CTConv(ut,'c_float_ptr')	
	_tDate = _CTConv(tDate,'c_int')
	_tut = _CTConv(tut,'c_float')	
	
	#call the C++ code
	return _CNearestTimeIndex(_n,_Date,_ut,_tDate,_tut)
