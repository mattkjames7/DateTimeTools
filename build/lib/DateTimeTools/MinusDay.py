import numpy as np
from ._CFunctions import _CMinusDay
from ._CTConv import _CTConv

def MinusDay(Date):
	'''
	Given an input day, this function will provide the date of the 
	preceeding day.
	
	Inputs
	======
	Date : int
		Date in the format yyyymmdd

		
	Returns
	=======
	Date : int
		Previous date in format yyyymmdd
	'''

	#convert the input into the exact dtype required for C++
	_Date = _CTConv(Date,'c_int')


	#call the C++ function
	return _CMinusDay(_Date)
	
