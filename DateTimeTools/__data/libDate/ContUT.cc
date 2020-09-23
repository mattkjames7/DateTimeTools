#include "ContUT.h"

/***********************************************************************
 * NAME : 		void PopulateYearUTC()
 * 
 * DESCRIPTION : 	Calculates the continuous time in hours since 00:00
 * 					on 19500101 for all years between 1950 and 2050
 * 
 * ********************************************************************/
void PopulateYearUTC() {
	
	int i, Year, nDays;
	bool ly;
	
	/* Set the first one to zero */
	YearUTC[0] = 0.0;
	
	/* Calculate the number of days since the last index */
	for (i=0;i<100;i++) {
		Year = i + 1950;
		LeapYear(1,&Year,&ly);
		if (ly) {
			nDays = 366;
		} else {
			nDays = 365;
		}
		YearUTC[i+1] = YearUTC[i] + ((double) nDays)*24.0;
	}
}


/***********************************************************************
 * NAME : 		void ContUT(n,Date,ut,utc)
 * 
 * DESCRIPTION : 	Calculates the continuous time in hours since 00:00
 * 					on 19500101 for an array of dates and times. NOTE:
 * 					This algorithm will probably work best if dates and 
 * 					times are arranges in chronological order.
 * 
 * INPUTS : 
 * 			int 	n			Number of elemenets in Date/ut arrays
 * 			int		Date		Date array
 * 			float	ut			Time array in decimal hours
 *
 * OUTPUTS :
 * 			double 	*utc		Continuous time in hours since 00:00 on
 * 								19500101
 * 
 * ********************************************************************/
void ContUT(int n, int *Date, float *ut, double *utc) {
	
	int i, Year, PrevDate;
	double dt, dtp;
	
	/* Start by working out what year it is */
	Year = Date[0]/10000;
	
	/* now get the starting utc */
	if ((Year >= 1950) & (Year <= 2050)) {
		dtp = YearUTC[Year - 1950];
		PrevDate = Year*10000 + 101
	} else if (Date < 1950) {
		dtp = YearUTC[0];
		PrevDate = 19500101;
	} else {
		dtp = YearUTC[100];
		PrevDate = 20500101;
	}
	
	/* copy the ut array and convert to double */
	for (i=0;i<n;i++) {
		utc[i] = (double) ut[i];
	}
	
	
}
