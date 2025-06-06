# DateTimeTools

A package containing some simple tools to manage dates and times.

## Installation

Installation requires `cmake` to be intalled in order to build `libdatetime`. It may be installed via `apt`:

```bash
sudo apt install cmake
```

or using `pip`:

```bash
pip3 install cmake
```

Install using `pip3`:

```bash
# Linux
pip3 install DateTimeTools

# MacOS
pip3 install DateTimeTools --no-build-isolation
```

NOTE: This module uses a C++ backend, which is compiled with CMake - please install CMake for your OS before installing this package.

## Usage

### Converting between different date/time formats

Usually this package deals with integer dates in the format `yyyymmdd` and floating point times in hours since the start of the day. 

We can convert to a few different time formats:

```python
import DateTimeTools as TT

Date = 20140102
ut = 15.0

#to unix time (seconds since 00:00 1970-01-01)
unixt = TT.UnixTime(Date,ut)
#and back
Date,ut = TT.UnixTimetoDate(unixt)

#to continuous time (hours since 00:00 1950-01-01)
utc = TT.ContUT(Date,ut)
#and back again
Date,ut = TT.contUTtoDate(utc)

#Julian day
jd = TT.JulDay(Date,ut)
#and back
Date,ut = TT.JulDaytoDate(jd)

#CDF Epoch (milliseconds since 00:00 0000-01-01)
cdfe = TT.CDFEpoch(Date,ut)
#and back
Date,ut = TT.CDFEpochtoDate(cdfe)

#get the python datetime
dt = TT.Datetime(Date,ut)
#or the reverse conversion
Date,ut = TT.DatetimetoDate(dt)

#convert hours since the start of the day to hours,minutes,seconds,milliseconds
hh,mm,ss,ms = TT.DectoHHMM(ut)
#and back
ut = TT.HHMMtoDec(hh,mm,ss,ms)

#Split dates into separate integers
yr,mn,dy = TT.DateSplit(Date)
#or the reverse
Date = TT.DateJoin(yr,mn,dy)
```



### Formatted plot tick marks

The `DTPlotLabel` function can be used to change the plot labels on the x-axis of a `matplotlib.pyplot` plot such that they resemble human-readable times and dates.

For example:

```python
import matplotlib.pyplot as plt

#some plot of a time series
#t is time either in unix time, ContUT, seconds from the start of the day
#or hours from the start of the day
plt.plot(t,x) 
ax = plt.gca()

#if we are plotting with t = TT.ContUT(Date,ut) 
#the function will be able to work out the date
#The TimeFMT keyword isn't needed here, by default = 'utc'
TT.DTPlotLabel(ax)

#similar to above - we can us unix time
#so t = TT.UnixTime(Date,ut)
#We must let the function know though
TT.DTPlotLabel(ax,TimeFMT='unix')

#With seconds from beginning of the day, we need to
#tell the function what Date starts at t == 0.0
#NOTE t can go beyond the range 0 < t < 24,
#the labels should include relevant dates
#Also, without the date keyword, just HH:MM(:SS) is shown
TT.DTPlotLabel(ax,TimeFMT='seconds',Date=20150101)

#Plotting with hours since the start of the day is similar
TT.DTPlotLabel(ax,TimeFMT='hours',Date=20190908)
```



### Calculating time differences

```python
#calculate the difference between two dates in days
ndays = TT.DateDifference(Date0,Date1)

#Similar to above, but include start and end times (still returns days)
ndays = TT.TimeDifference(Date0,ut0,Date1,ut1)

#We can find the middle time between two date/times
mDate,mut = TT.MidTime(Date0,ut0,Date1,ut1)
```



### Filtering time series data

Given an evenly sampled time series, the `lsfilter` function can perform low-pass and high-pass filtering.

```python
#t is the evenly smapled time axis
#x is the time series data

#we need to know the sampling interval in seconds
inter = t[1] - t[0]

#we can do a low-pass filter, we need to set 'high = inter'
#and 'low = lsec' which is the cutoff period in seconds
xlow = TT.lsfilter(x,inter,lowsec,inter)

#alternatively a high-pass filter can be used by setting
#'high = hsec' (the cutoff period in seconds) and 'low = inter'
xhigh = TT.lsfilter(x,hsec,inter,inter)
```





### Miscellaneous functions

```python
#calculate day number and year
year,dayno = TT.DayNo(Date)
#or return to original date format
Date = TT.DayNotoDate(year,dayno)

#Check if year(s) are leap year(s)
ly = TT.LeapYear(year)

#Add one day to a date
NextDate = TT.PlusDay(Date)
#or go back a day
PrevDate = TT.MinusDay(Date)

#Calculate the nearest index in a time/date array
#to a test time/date
ind = TT.NearestTimeIndex(DateArray,utArray,testDate,testut)

#check which indices of a time array are within two time limits
inds = TT.WithinTimeRange(t,t0,t1)
#or including dates
inds = TT.WithinTimeRange((d,t),(d0,t0),(d1,t1))
#alternatively, return a boolean array where each True element is within the range
b = TT.WithinTimeRange((d,t),(d0,t0),(d1,t1),BoolOut=True)
```







