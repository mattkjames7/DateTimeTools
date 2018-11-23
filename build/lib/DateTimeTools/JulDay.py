import numpy as np

def JulDay(Date,ut=12.0):
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
