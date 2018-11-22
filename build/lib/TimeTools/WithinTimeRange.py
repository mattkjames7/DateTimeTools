import numpy as np

def WithinTimeRange(Timet,Time0,Time1):
	'''
	Performs a simple check on a test time (Timet) to see if it exists
	between Time0 and time1.
	
	Inputs:
		Timet: Test time - either a single floating point (array or 
		scalar) to denote hours of the day, or a tuple containing 
		(Date,Time).
		Time0: Start time, same format as above.
		Time1: End time, same format as above.
		
	Output:
		boolean (array or scalar), True if within time range.
	'''
	sh = np.shape(Timet)
	s0 = np.size(Time0)
	s1 = np.size(Time1)
	
	if s0 == 2:
		D0 = Time0[0]
		T0 = Time0[1]
	else:
		T0 = Time0
		D0 = 0
		
	if s1 == 2:
		D1 = Time1[0]
		T1 = Time1[1]
	else:
		T1 = Time1
		D1 = 0	
	
	if sh[0] == 2 and np.size(sh) == 2:
		#hopefully this is a list of date and time
		D = np.array([Timet[0]]).flatten()
		T = np.array([Timet[1]]).flatten()
		res = np.zeros(sh[1],dtype='bool')
		if D0 == D1:
			use = np.where((D == D0) & (T >= T0) & (T <= T1))[0]
		else:
			use = np.where(((D == D0) & (T >= T0)) | ((D == D1) & (T <= T1)) | ((D > D0) & (D < D1)))[0]
		res[use] = True
		
	else:
		#just time
		T = np.array([Timet]).flatten()
		res = np.zeros(sh[0],dtype='bool')
		use = np.where((T >= T0) & (T <= T1))[0]
		res[use] = True

	return res
