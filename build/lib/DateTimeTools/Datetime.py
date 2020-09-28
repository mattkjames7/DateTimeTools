import numpy as np
import datetime
from .DectoHHMM import DectoHHMM
from .DateSplit import DateSplit


def Datetime(Date,ut):
	'''
	Convert dates and times to datetime objects.
	
	Inputs
	======
	Date : int
		Date array in the format yyyymmdd
	ut : float
		Time array in hours since start of hte day
	
	Returns
	=======
	dt : datetime
		Array of datetimes
	
	'''
	
	#split the daates and time
	yr,mn,dy = DateSplit(Date)
	hh,mm,ss,ms = DectoHHMM(ut)	
	ms = ms.astype('int32')
	
	#create the datetime arrays
	n = yr.size
	dt = np.array([datetime.datetime(yr[i],mn[i],dy[i],hh[i],mm[i],ss[i],ms[i]*1000) for i in range(0,n)])
		
	return dt
	
