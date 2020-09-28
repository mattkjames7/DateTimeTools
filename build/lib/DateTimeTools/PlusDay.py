import numpy as np
from ._CFunctions import _CPlusDay
from ._CTConv import _CTConv

def PlusDay(Date):
	'''
	Given an input day, this function will provide the date of the 
	following day.
	
	Inputs
	======
	Date : int
		Date in the format yyyymmdd

		
	Returns
	=======
	Date : int
		Following date in format yyyymmdd
	'''

	#convert the input into the exact dtype required for C++
	_Date = _CTConv(Date,'c_int')


	#call the C++ function
	return _CPlusDay(_Date)
	
