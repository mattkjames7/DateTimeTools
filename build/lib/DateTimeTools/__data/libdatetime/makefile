all: o lib

o:
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
	#g++ -c -fPIC WhereEq.cc
	#g++ -c -fPIC BubbleSort.cc
	g++ -c -fPIC -fPIC ContUT.cc
	g++ -c -fPIC -fPIC UnixTime.cc
	#g++ -c -fPIC Unique.cc
	g++ -c -fPIC NearestTimeIndex.cc
	g++ -c -fPIC WithinTimeRange.cc
	g++ -c -fPIC JulDay.cc
	g++ -c -fPIC JulDaytoDate.cc

lib: 
	g++ -shared -fPIC -o libdatetime.so *.o

clean:
	rm -v *.o *.so
