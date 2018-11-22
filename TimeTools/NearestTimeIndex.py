import numpy as np
from .TimeDifference import TimeDifference

def NearestTimeIndex(D,T,Dt,Tt):
	'''
	Finds the array index of the closest point in time, within a series 
	of dates and times.
	
	Inputs:
		D: Date array.
		T: Time Array.
		Dt: test date.
		Tt: test time.
		
	Returns:
		Integer index of closest date/time (D,T) to the test date/time
		(Dt,Tt).
	'''
	
	#reduce to nearest date first
	Ddiff = np.abs(D-Dt)
	use = np.where(Ddiff == np.min(Ddiff))[0]
	if use.size == 1:
		return use[0]
	
	t = T[use]
	d = D[use]
	
	n = np.size(t)
	dt = np.zeros(n,dtype='float32')
	for i in range(0,n):
		dt[i] = TimeDifference(d[i],t[i],Dt,Tt)
	
	use2 = np.where(np.abs(dt) == np.min(np.abs(dt)))[0]
	if use2.size == 1:
		return use[use2[0]]
	else:
		return use[use2]
		
	
	
