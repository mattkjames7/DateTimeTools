import numpy as np
from .DateTools import DateDifference

def TimeDifference(D0,T0,D1,T1):
	'''
	Calculates the time difference between two dates and times.
	
	Inputs:
		D0: Start date, format YYYYMMDD.
		T0: Floating point start time in hours.
		D1: End date, format YYYYMMDD.
		T1: End time, floating point hours.
		
	Returns:
		Time difference in days (floating point), where positive values 
		imply that D0,T0 is before D1,T1.
	'''
	dd = DateDifference(D0,D1)
	tdiff = dd + (T1-T0)/24.0
	return tdiff
