import numpy as np
import cdflib
from .DectoHHMM import DectoHHMM
from .DateSplit import DateSplit

def CDFEpoch(Date,ut):
	'''
	Converts date and time to CDF Epoch - which is the number of 
	milliseconds since 00000101 00:00
	
	Inputs
	======
	Date : int
		Array of dates int he format yyyymmdd
	ut : float
		Array of times since the start of the day in hours
	
	Returns
	=======
	cdfe : double
		CDF Epoch
	
	'''
	
	#split the date and time
	yr,mn,dy = DateSplit(Date)
	hh,mm,ss,ms = DectoHHMM(ut)
	
	#now create an array which can be accepted by cdflib
	dt = np.array([yr,mn,dy,hh,mm,ss,ms]).T
	
	#convert
	cdfe = cdflib.cdfepoch.compute_epoch(dt)
	
	return cdfe
	
	
	
	
