import numpy as np
from ._CFunctions import _CJulDay
from ._CTConv import _CTConv

def JulDay(Date,ut):
	'''
	Converts date and time into Julian date
	
	Inputs
	======
	Date : int
		Array or scalar of dates
	ut : float
		Array or scalar of times in hours since the start of the day
		
	Returns
	=======
	jd : float64
		Julian date
	'''

	#convert the inputs into the exact dtypes required for C++
	_n = _CTConv(np.size(ut),'c_int')
	_Date = _CTConv(Date,'c_int_ptr')
	_ut = _CTConv(ut,'c_float_ptr')
	_jd = np.zeros(_n,dtype='float64')

	#call the C++ function
	_CJulDay(_n,_Date,_ut,_jd)
	
	return _jd





def JulDayOld(Date,ut=12.0):
	'''
	Convert Date and time into Julian day.
	'''
	year = np.int32(Date/10000)
	month = np.int32((Date % 10000)/100)
	day = Date % 100
	
	a = np.int32((14-month)/12)
	y = year + 4800 - a
	m = month + 12*a - 3
	
	JDN = day + np.int32((153*m + 2)/5) + 365*y + np.int32(y/4) - np.int32(y/100) + np.int32(y/400) - 32045 + ut/24.0 - 0.5
	return JDN
