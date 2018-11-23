import datetime
import numpy as np
from .DateTools import MinusDay

def UT2datetime(indate,inut):
	'''
	Converts date of the format YYYYMMDD and time in floating point 
	hours to a datetime object.
	
	'''
	if np.size(indate) == 1:
		date = np.zeros(np.size(inut),dtype='int32')+indate
	else:
		date = np.int32(indate)
	
	if np.size(inut) == 1:
		ut = np.float32([inut])
	else:
		ut = np.float32(inut)	
		
		
	for i in range(0,np.size(ut)):
		if ut[i] < 0:
			ut[i]+=24.0
			date[i] = MinusDay(date[i])
	
	yr=np.int32(date/10000)
	mn=np.int32((date % 10000)/100)
	dy=date % 100
	
	hh=np.int32(ut)
	mmf=(ut-hh)*60
	mm=np.int32(mmf)
	ssf=(mmf-mm)*60.0
	ss=np.int32(ssf)
	ms=np.int32((ssf-ss)*1000000.0)
	
	
	dt=np.array([datetime.datetime(yr[i],mn[i],dy[i],hh[i],mm[i],ss[i],ms[i]) for i in range(0,np.size(ut))])
		
	return dt

def datetime2UT(DT):
	'''
	Converts datetime objects to arrays of dates with the format 
	YYYYMMDD and times in floating point hours. 
	'''
	if hasattr(DT,'__iter__'):
		n = np.size(DT)
		ut = np.zeros(n,dtype='float32')
		date = np.zeros(n,dtype='int32')
		for i in range(0,n):
			ut[i] = np.float32(DT[i].hour) + np.float32(DT[i].minute)/60.0 + np.float32(DT[i].second)/3600.0
			date[i] = np.int32(DT[i].year)*10000 + np.int32(DT[i].month)*100 + np.int32(DT[i].day)			
	else:
		ut = np.float32(DT.hour) + np.float32(DT.minute)/60.0 + np.float32(DT.second)/3600.0
		date = np.int32(DT.year)*10000 + np.int32(DT.month)*100 + np.int32(DT.day)
		
	return (date,ut)
