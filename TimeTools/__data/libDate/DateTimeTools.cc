#include "DateTimeTools.h"

int LeapYear(int *year, int n, bool res) {
	int i;
	for (i=0;i<n;i++) {
		if (((year[i] % 4) == 0 && (year[i] % 100) != 0) || (year[i] % 400) == 0) {
			res[i] = true;
		} else {
			res[i] = false;
		}
	}
}
		

void DateToYearDayNo(int *Date, int n, int *Year, int *DayNo) {
	int Month, Day, i;
	bool ly[n];
	LeapYear(Year,n,ly);
	int months[13] = {0,31,59,90,120,151,181,212,243,273,304,334,365};
	for (i=0;i<n;i++) {
		Year[i] = Date[i]/10000;
		Month=(Date[i] % 10000)/100;
		Day=Date[i] % 100;
		if (ly[i] && Month > 2) {
			DayNo[i] = months[Month-1] + Day + 1;
		} else {
			DayNo[i] = months[Month-1] + Day;
		}
	}
	
}

void DecUTToHHMMSS(float *UT, int n, int *H, int *M, int *S, float *MS) {
	int i;
	float Md, Sd;
	for (i=0;i<n;i++) {
		H[i] = (int) UT[i];
		Md = (60.0*(UT[i] - H[i]));
		M[i] = (int) Md;
		Sd = (60.0*(Md - M[i]));
		S[i] = (int) Sd;
		MS[i] = (Sd - S[i])*1000.0;
	}
}

void HHMMSSUTToDec(int *H, int *M, int *S, float *MS, int n, float *UT) {
	int i;
	for (i=0;i<n;i++) {
		UT[i] = H[i] + M[i]/60.0 + S[i]/3600.0 + MS[i]/3600000.0;
	}
}


int DayNotoDate(int *Year, int *Doy, int n, int *Date) {
	int monthsly[13] = {0,31,60,91,121,152,182,213,244,274,305,335,366};
	int monthsny[13] = {0,31,59,90,120,151,181,212,243,273,304,334,365};
	int *months, i;
	int j, mn, dy;
	bool ly[n];
	LeapYear(Year,n,ly);
	for (i=0;i<n;i++) {
		if (ly[i]) {
			months = monthsly;
		} else {
			months = monthsny;
		}
		
		if (Doy > months[12]) {
			Date[i] = Year*10000 + 1231;	
		} else {
			
			j=0;
			mn=0;
			dy=Doy[i];
			while ((Doy[i] > months[j]) && (mn < 12)) {
				mn=j+1;
				dy=Doy[i]-months[j];
				j++;
			}
			Date[i] = Year[i]*10000+mn*100+dy;
		}
	}
}

int PlusDay(int Date){
	int doy, tmp_year, out;
	bool ly;
	DateToYearDayNo(Date,&tmp_year,&doy);
	LeapYear(&tmp_year,1,&ly);
	if (((ly == 1) && (doy == 366)) || ((!ly) && (doy == 365))) {
		doy = 1;
		tmp_year++;
	} else {
		doy++;
	}
	DayNotoDate(&tmp_year,&doy,1,out);
	return out;
}

int MinusDay(int Date):
	int doy, tmp_year, out, new_doy;
	bool ly;
	DateToYearDayNo(Date,&tmp_year,&doy);
	
	if (doy == 1) {
		temp_year=date/10000 - 1;
		LeapYear(&tmp_year,1,&ly);
		if (ly) {
			new_doy=366;
		} else {
			new_doy=365;
		}
		DayNotoDate(&temp_year,&new_doy,1,&out);
	} else {
		new_doy=doy-1;
		temp_year=date/10000;
		DayNotoDate(&temp_year,&new_doy,1,&out)
	}
	return out;
}

int DateDifference(int Date0, int Date1) {
	int SD, ED, dd, Dir;
	if (Date0 > Date1) {
		SD = Date1;
		ED = Date0;
		Dir = -1;
	} else { 
		SD = Date0;
		ED = Date1;
		Dir = 1;
	}
	
	dd = 0;
	while (SD < ED) {
		SD = PlusDay(SD);
		dd += Dir;
	}
	return dd;
}

float TimeDifference(int Date0, float ut0, int Date1, float ut1) {
	int dd = DateDifference(Date0,Date1);
	return ((float) dd) + (ut1 - ut0)/24.0;
}

void DateSplit(int n, int *Date, int *yyyy, int *mm , int *dd) {
	int i;
	for (i=0;i<n;i++) {
		yyyy[i] = Date[i]/10000;
		mm[i] = (Date[i] % 10000)/100;
		dd[i] = Date[i] % 100;
	}
}

void DateCat(int n, int *yyyy, int *mm, int *dd, int *Date) {
	int i;
	for (i=0;i<n;i++) {
		Date[i] = yyyy[i]*10000 + mm[i]*100 + dd[i];
	}
}
