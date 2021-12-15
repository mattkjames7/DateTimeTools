@echo off
where /q g++
if %ERRORLEVEL% neq 0 (
	echo g++ not found
	exit /b 6
)

echo Attempting to compile libdatetime

g++ -c -fPIC hhmm.cc
g++ -c -fPIC LeapYear.cc
g++ -c -fPIC DateSplit.cc
g++ -c -fPIC DateJoin.cc
g++ -c -fPIC DayNo.cc
g++ -c -fPIC PlusDay.cc
g++ -c -fPIC MinusDay.cc
g++ -c -fPIC DateDifference.cc
g++ -c -fPIC TimeDifference.cc
g++ -c -fPIC MidTime.cc
g++ -c -fPIC ContUT.cc 
g++ -c -fPIC UnixTime.cc
g++ -c -fPIC NearestTimeIndex.cc
g++ -c -fPIC WithinTimeRange.cc
g++ -c -fPIC JulDay.cc
g++ -c -fPIC JulDaytoDate.cc



g++ -shared -fPIC -o libdatetime.dll *.o


del *.o

if %ERRORLEVEL% neq 0 (
	echo Compilation failed
	exit /b 7
)
echo Done

exit /b 0
@echo on

