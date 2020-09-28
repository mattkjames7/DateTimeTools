import numpy as np
import cdflib
from .HHMMtoDec import HHMMtoDec
from .DateJoin import DateJoin


def CDFEpochtoDate(cdfe):
	'''
	Computes the date and time from the CDF Epoch (milliseconds since
	Jan 01 0000).
	
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
	dt = cdflib.cdfepoch.breakdown_epoch(cdfe).T
	
	#extract dates and times
	Date = DateJoin(dt[0],dt[1],dt[2])
	ut = HHMMtoDec(dt[3],dt[4],dt[5],dt[6])
	
	return Date,ut
