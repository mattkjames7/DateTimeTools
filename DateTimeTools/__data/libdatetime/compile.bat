@echo off

where /q g++
if %ERRORLEVEL% neq 0 (
	echo G++ wasn't found
	exit /b 9
)

echo Compiling libdatetime...

g++ -c -fPIC hhmm.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC LeapYear.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC DateSplit.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC DateJoin.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC DayNo.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC PlusDay.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC MinusDay.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC DateDifference.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC TimeDifference.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC MidTime.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
@REM g++ -c -fPIC WhereEq.cc
@REM if %ERRORLEVEL% neq 0 (goto CompileError)
@REM g++ -c -fPIC BubbleSort.cc
@REM if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC ContUT.cc 
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC  UnixTime.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
@REM g++ -c -fPIC Unique.cc
@REM if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC NearestTimeIndex.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC WithinTimeRange.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC JulDay.cc
if %ERRORLEVEL% neq 0 (goto CompileError)
g++ -c -fPIC JulDaytoDate.cc
if %ERRORLEVEL% neq 0 (goto CompileError)

g++ -shared -fPIC -o libdatetime.dll hhmm.o LeapYear.o DateSplit.o DateJoin.o DayNo.o PlusDay.o MinusDay.o DateDifference.o TimeDifference.o MidTime.o ContUT.o UnixTime.o NearestTimeIndex.o WithinTimeRange.o JulDay.o JulDaytoDate.o -Wall
if %ERRORLEVEL% neq 0 (goto CompileError)

echo Done

del *.o
exit /b 0

:CompileError
echo Compilation error
exit /b 8