import numpy as np

def LeapYear(year):
	'''
	Returns True if year is a leap year, False otherwise. Should also work for numpy arrays.
	'''
	return ((((year % 4) == 0) & ((year % 100) != 0)) | ((year % 400) == 0))

		
def DayNo(date):
	'''
	Calculates the day number for a given date of the format YYYYMMDD.
	'''
	year=np.int32(date/10000)
	month=np.int32((date % 10000)/100)
	day=date % 100
	start_day= np.array([  0, 31, 59, 90,120,151,181,212,243,273,304,334])
	dayno = start_day[month-1] + day + np.int32(LeapYear(year) & (month > 2))
	
#	if LeapYear(year) and month > 2:
#		dayno=start_day[month-1]+day+1
#	else:
#		dayno=start_day[month-1]+day
	return dayno

def DayNotoDate(year,doy):
	'''
	This function will return a date of the format YYYYMMDD given a year
	and a day number.
	
	Inputs:
		year: Integer year.
		doy: Integer day number.
		
	Output:
		Date: integer date with format YYYYMMDD
	'''
	if LeapYear(year):
		months=[0,31,60,91,121,152,182,213,244,274,305,335,366]
	else:
		months=[0,31,59,90,120,151,181,212,243,273,304,334,365]
	
	if doy > months[12]:
		return np.int32(year)*10000 + np.int32(1231)	
	i=0
	mn=0
	dy=doy
	while doy > months[i] and mn < 12:
		mn=i+1
		dy=doy-months[i]
		i+=1
		
	return np.int32(year*10000+mn*100+dy)

def PlusDay(date):
	'''
	This function adds a single day to a given date.
	'''
	doy=DayNo(date)
	temp_year=np.int32(date/10000)
	ly=LeapYear(temp_year)
	
	if (ly and (doy == 366)) or (not ly and (doy == 365)):
		new_doy=1
		temp_year+=1
	else:
		new_doy=doy+1
		
	new_date=DayNotoDate(temp_year,new_doy)
	return new_date
	
def MinusDay(date):
	'''
	This function will return the date prior to the date input.
	'''
	doy=DayNo(date)
	if doy == 1:
		temp_year=np.int32(date/10000) - 1
		ly=LeapYear(temp_year)
		if ly:
			new_doy=366
		else:
			new_doy=365
		
		new_date=DayNotoDate(temp_year,new_doy)
	else:
		new_doy=doy-1
		temp_year=np.int32(date/10000)
		new_date=DayNotoDate(temp_year,new_doy)
	return new_date
		
	
def PlusDate(year,month,day):
	'''
	This function will add one day to the date input.
	
	Inputs:
		year,month,day: integers
	
	Output:
		year,month,day
	'''
	date=np.int32(year*10000 + month*100 + day)
	
	doy=DayNo(date)
	temp_year=np.int32(date/10000)
	ly=LeapYear(temp_year)
	
	if (ly and (doy == 366)) or (not ly and (doy == 365)):
		new_doy=1
		temp_year+=1
	else:
		new_doy=doy+1
		
	new_date=DayNotoDate(temp_year,new_doy)
	
	yy=np.int32(new_date/10000)
	mm=np.int32((new_date-yy*10000)/100)
	dd=new_date % 100
	
	return (yy,mm,dd)
	
	
def DateDifference(StartDate,EndDate):
	'''
	This function calculates the difference between two dates.
	
	Returns difference in days, where positive implies that EndDate is
	after StartDate and negative difference implies the converse. 
	'''
	if StartDate > EndDate:
		SD = EndDate
		ED = StartDate
		Dir = -1
	else:
		SD = StartDate
		ED = EndDate
		Dir = 1
		
	dd = 0
	while (SD < ED):
		SD = PlusDay(SD)
		dd += Dir
	
	return dd
	
	
def DateSplit(Date):
	'''
	This function splits a date integer of the format YYYYMMDD, returns
	three integers containing year, month and day.
	'''
	yr = np.int32(Date/10000)
	mn = np.int32(Date/100 % 100)
	dy = np.int32(Date % 100)
	return (yr,mn,dy)
