import numpy as np
from .HHMMtoDec import HHMMtoDec
from .DateJoin import DateJoin
import datetime

def DatetimetoDate(dt):
	'''
	Convert datetime objects to dates and times
	
	Inputs
	======
	dt : datetime
		Array of datetimes

	Returns
	=======
	Date : int
		Date array in the format yyyymmdd
	ut : float
		Time array in hours since start of the day
	
	
	'''
	
	#convert to array
	if not isinstance(dt,np.ndarray):
		_dt = np.array([dt])
	else:
		_dt = dt
		
	#extract the components
	n = _dt.size
	yr = np.zeros(n,dtype='int32')
	mn = np.zeros(n,dtype='int32')
	dy = np.zeros(n,dtype='int32')
	hh = np.zeros(n,dtype='int32')
	mm = np.zeros(n,dtype='int32')
	ss = np.zeros(n,dtype='int32')
	ms = np.zeros(n,dtype='float32')
	for i in range(0,n):
		yr[i] = _dt[i].year
		mn[i] = _dt[i].month
		dy[i] = _dt[i].day
		hh[i] = _dt[i].hour
		mm[i] = _dt[i].minute
		ss[i] = _dt[i].second
		ms[i] = _dt[i].microsecond/1000.0

	#join the dates and times back up
	Date = DateJoin(yr,mn,dy)
	ut = HHMMtoDec(hh,mm,ss,ms)
	
	return Date,ut
