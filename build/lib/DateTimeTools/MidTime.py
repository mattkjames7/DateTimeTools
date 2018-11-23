import numpy as np
from .DateTools import PlusDay,DateDifference

def MidTime(Date0,ut0,Date1,ut1):
	'''
	Calculate the midpoint in time between two dates and times.
	
	Inputs:
		Date0: Start date with format YYYYMMSS.
		ut0: Start time, floating point hours.
		Date1: End date with format YYYYMMSS.
		ut1: End time in floating point hours.
		
	Returns:
		mDate: Date at mid point.
		mut: Floating point time at midpoint.
	'''
	dDay = DateDifference(Date0,Date1)
	
	if dDay == 0:
		return Date0,0.5*(ut0+ut1)
	else:
		dHour = dDay*24.0 - ut0 + ut1
		nDayHalf = np.int32((dHour/2+ut0)/24.0)
		mDate = Date0
		for i in range(0,nDayHalf):
			mDate = PlusDay(mDate)
			
		mut = (dHour/2 + ut0) % 24.0
		return mDate,mut
		
		
		
		
