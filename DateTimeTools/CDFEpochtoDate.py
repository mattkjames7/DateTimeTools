import numpy as np
import cdflib
from .HHMMtoDec import HHMMtoDec
from .DateJoin import DateJoin


def CDFEpochtoDate(cdfe):
	'''
	Computes the date and time from the CDF Epoch.
	
	Inputs
	======
	cdfe : float
		The CDF Epoch array
		
	Returns
	=======
	Date : int
		Array of dates in the format yyyymmdd
	ut : float
		Array of times in hours since the beginning of the day
		
	
	'''

	#convert using cdflib
	dt = cdflib.cdfepoch.breakdown(cdfe).T
	
	#check if there is more time information than just ms
	if dt.shape[0] == 9:
		ms = dt[6] + dt[7]/1000.0 + dt[8]/1000000.0
	else:
		ms = dt[6]
		
	#extract dates and times
	Date = DateJoin(dt[0],dt[1],dt[2])
	ut = HHMMtoDec(dt[3],dt[4],dt[5],ms)
	
	return Date,ut
