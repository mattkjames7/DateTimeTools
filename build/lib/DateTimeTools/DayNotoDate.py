import numpy as np
from ._CFunctions import _CDayNotoDate
from ._CTConv import _CTConv

def DayNotoDate(Year,Doy):
	'''
	Converts year and day numbers to a date of the format yyyymmdd.
	
	Inputs
	======
	Year : int32
		Array or scalar of years
	Doy : int32
		Array or scalar of day numbers
		
	Returns
	=======
	Date : int
		Array or scalar of dates
		
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(ut),'c_int')
	_Year = _CTConv(Year,'c_int_ptr')
	_Doy = _CTConv(Doy,'c_int_ptr')
	_Date = np.zeros(_n,dtype='int32')

	#call the C++ function
	_CDayNotoDate(_n,_Year,_Doy,_Date)
	
	return _Date
