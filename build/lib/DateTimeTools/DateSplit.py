import numpy as np
from ._CFunctions import _CDateSplit
from ._CTConv import _CTConv

def DateSplit(Date):
	'''
	Splits an array of dates in the format yyyymmdd into arrays of 
	years, months and days.
	
	Inputs
	======
	Date : int32
		Array or scalar of dates in the format yyyymmdd.

	Returns
	=======
	Year : int
		Array or scalar of years
	Month : int
		Array or scalar of months
	Day : int
		Array or scalar of days
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(Date),'c_int')
	_Date = _CTConv(Date,'c_int_ptr')
	_Year = np.zeros(_n,dtype='int32')
	_Month = np.zeros(_n,dtype='int32')
	_Day = np.zeros(_n,dtype='int32')

	#call the C++ function
	_CDateSplit(_n,_Date,_Year,_Month,_Day)
	
	return _Year,_Month,_Day
