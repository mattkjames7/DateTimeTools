import numpy as np

def DectoHHMM(ut,ss=False,ms=False,Split=False):
	'''
	Convert decimal time in hours to separate hours, minutes etc.
	
	Inputs:
		ut:	floating point array of times.
		ss:	If True, seconds are included in the output.
		ms: If True, milliseconds are also included in the output.
		Split: If True, a tuple of (hours,minutes,seconds,milliseconds)
			   is returned, otherwise an integer will be returned with 
			   the format HHMMSSMS
			   
	Returns:
		Tuple of hours,minutes,seconds,milliseconds, or an integer of 
		the forma HHMMSSMS.
	'''
	hh=np.int32(np.floor(ut))
	mm=np.int32(np.floor((ut-hh)*60.0))
	s=np.int32(np.floor(((ut-hh)*60-mm)*60))
	m=np.int32(np.floor((((ut-hh)*60-mm)*60-s)*1000))
	
	if Split == True:
		if ms:
			return (hh,mm,s,m)
		elif ss:
			return (hh,mm,s)
		else:
			return (hh,mm)
	else:
		out = (hh*100+mm)
		if ms:
			out = (out*100+s)*1000+m
		elif ss:
			out = out*100+s
		
		return out
			
def HHMMtoDec(ut,ss=False,ms=False):
	'''
	This function converts input integer times with the format HHMM 
	(or HHMMSS, HHMMSSMS) to a floating point time HH.HHH
	
	Inputs:
		ut: input time integer, HHMM.
		ss: If True, then input is treated as having format HHMMSS.
		ms: If True, input is treated as having format HHMMSSMS.
		
	Output:
		Floating point time, returns array if input is an array.
	'''
	t = np.copy(ut)
	m = 0
	s = 0
	if ms == True:
		m = ut % 1000
		ut = np.int32(ut//1000)
	if ss == True:
		s = ut % 100
		ut = np.int32(ut//100)		
	hh = np.int32(ut//100)
	mm = ut % 100

	out=np.float32(hh)+np.float32(mm)/60+np.float32(s)/3600+np.float32(m)/3600000
	return out
