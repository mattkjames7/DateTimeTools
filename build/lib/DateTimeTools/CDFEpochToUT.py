import numpy as np

def CDFEpochToUT(DT):
	'''
	This function should convert CDFEpoch time to an array of dates (of
	the format YYYYMMDD) and and array of times in hours (hh.hhh).
	
	Input:
		DT: numpy array of CDF Epochs
		
	Outputs:
		Date: array of dates
		ut: array of times
	
	'''
	#convert to strings if need be
	if DT.dtype in ['datetime64[ms]','<M8[ns]']:
		dt = DT.astype('U')
	else:
		dt = DT
		
	year = np.int32([x[0:4] for x in dt])
	month = np.int32([x[5:7] for x in dt])
	day = np.int32([x[8:10] for x in dt])
	Date = year*10000 + month*100 + day
	
	hour = np.float32([x[11:13] for x in dt])
	minute = np.float32([x[14:16] for x in dt])
	second = np.float32([x[17:29] for x in dt])
	ut = hour + minute/60.0 + second/3600.0
	
	return (Date,ut)
