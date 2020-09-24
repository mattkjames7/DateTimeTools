import numpy as np
from ._CFunctions import _CDateJoin
from ._CTConv import _CTConv

def DateJoin(Year,Month,Day):
	'''
	Combines lists of years, months and days to form an array of dates
	with the format yyyymmdd.
	
	Inputs
	======
	Year : int
		Array or scalar of years
	Month : int
		Array or scalar of months
	Day : int
		Array or scalar of days

	Returns
	=======
	Date : int32
		Array or scalar of dates in the format yyyymmdd.
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(Year),'c_int')
	_Year = _CTConv(Year,'c_int_ptr')
	_Month = _CTConv(Month,'c_int_ptr')
	_Day = _CTConv(Day,'c_int_ptr')
	_Date = np.zeros(_n,dtype='int32')

	#call the C++ function
	_CDateJoin(_n,_Year,_Month,_Day,_Date)
	
	return _Date
