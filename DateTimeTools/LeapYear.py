import numpy as np
from ._CFunctions import _CLeapYear
from ._CTConv import _CTConv

def LeapYear(Year):
	'''
	Determines whether a year or years are leap years
	
	Inputs
	======
	Year : int
		Array or scalar of years

		
	Returns
	=======
	ly : bool
		Array of boolean, where True means is was a leap year
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(Year),'c_int')
	_Year = _CTConv(Year,'c_int_ptr')
	_ly = np.zeros(_n,dtype='bool')

	#call the C++ function
	_CLeapYear(_n,_Year,_ly)
	
	return _ly
