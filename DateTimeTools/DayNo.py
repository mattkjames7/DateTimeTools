import numpy as np
from ._CFunctions import _CDayNo
from ._CTConv import _CTConv

def DayNo(Date):
	'''
	Converts date to year and day number.
	
	Inputs
	======
	Date : int
		Array or scalar of dates
		
	Returns
	=======
	Year : int32
		Array or scalar of years
	Doy : int32
		Array or scalar of day numbers
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(ut),'c_int')
	_Date = _CTConv(Date,'c_int_ptr')
	_Year = np.zeros(_n,dtype='int32')
	_Doy = np.zeros(_n,dtype='int32')

	#call the C++ function
	_CDayNo(_n,_Date,_Year,_Doy)
	
	return _Year,_Doy
