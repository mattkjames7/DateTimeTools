import numpy as np
from ._CFunctions import _CDateDifference
from ._CTConv import _CTConv

def DateDifference(Date0,Date1):
	'''
	Calculates the time difference between two given dates.
	
	Inputs
	======
	Date0 : int
		Start date, format YYYYMMDD.
	Date1 : int
		End date, format YYYYMMDD.
		
	Returns
	=======
	nDays : int32
		Time difference in days where positive values imply that Date0 is 
		before Date1.
	'''

	#convert the data types
	_Date0 = _CTConv(Date0,'c_int')
	_Date1 = _CTConv(Date1,'c_int')


	#run the C++ routine
	return _CDateDifference(_Date0,_Date1)
	
