import numpy as np
from .ContUT import ContUT
from .ContUTtoDate import ContUTtoDate
from .DateSplit import DateSplit
from .DectoHHMM import DectoHHMM

def DTPlotLabel(fig,Seconds=False,IncludeYear=True,TickFreq='default',
				TimeFMT='utc',ShowDate=True,Date=None):
	'''
	Simple subroutine to convert the time axis of a plot to show human 
	readable times and dates, hopefully!
	
	Inputs
	======
	fig : object
		Either an instance of pyplot or pyplot.Axes passed to the 
		function, useful for plotting multiple figures on one page,
		or overplotting
	Seconds : bool
		Show seconds in the time format.
	IncludeYear : bool
		Show the year in the date.  
	TickFreq : str | float
		This will control the frequency at which tick marks appear, with
		the following options:
		'default' : This will just do a straight swap of the labels 
					without moving the tick marks
		'auto' : 	This option will automatically change the frequency
					based upon the time range.
		float : 	Given a real number, the tick marks will be spaced
					by this number in hours
	TimeFMT : str
		This has a few options:
		'utc' : continuous time in hours since 19500101
		'unix' : Unix time - time in seconds since 19700101
		'hours' : this is just hours from the beginning of the day,
				if the Date keyword is set then where the time = 0 will
				be treated as the start of the date supplied Date, 
				otherwise we will not print a date
		'seconds' :  This is similar to 'hours' except that the time
				is expected to be in seconds from the start of the day.
	ShowDate : bool
		If True, then dates will be shown on tick mark labels, otherwise
		it will only show times.
	Date : int
		single integer date in the format yyyymmdd corresponding to the
		date when the time axis = 0.0.
	'''
	#firstly check if this is a pyplot or pyplot.Axes instance
	if hasattr(fig,'gca'):
		ax = fig.gca()
	else:
		ax = fig
		
	#get the time range and tick mark locations
	trnge = np.array(ax.get_xlim())
	print(trnge)
	tlen = (trnge[1] - trnge[0])	
	mt = ax.xaxis.get_majorticklocs()
	
	#convert the time based on the TimeFMT keyword
	if TimeFMT in ['seconds','unix']:
		ConvTime = True
		trnge /= 3600.0
		tlen /= 3600.0
		mt /= 3600.0
	else:
		ConvTime = False


	#check if we need to alter stuff to convert the times to ContUT
	dt = 0.0
	if TimeFMT in ['seconds','hours']:
		if Date is None:
			#no date supplied, so we need to make sure we don't try to 
			# plot a date
			ShowDate = False
		else:
			dt = ContUT(Date,0.0)
	elif TimeFMT == 'unix':
		#time should already be converted to hours, now we need to work
		#out the amount ot time difference between 1950 and 1970
		dt = ContUT(19700101,0.0) 	
		print(dt)
	trnge += dt
	tlen += dt
	mt += dt
				
	#recalculate the tick frequency if needed
	if not TickFreq == 'default':
		#set the tick frequency in hours
		if TickFreq == 'auto':
			tfs = np.array([1440.0,720.0,360.0,240.0,180.0,120.0,60.0,30.0,15.0,10.0,5.0,2.0,1.0])
			dtf = np.abs(60.0*tlen/tfs - 5.0)
			use = np.where(dtf == np.min(dtf))[0][0]
			tf = tfs[use]/60.0
		else: 
			#use custom tick frequency
			tf = TickFreq
		#work out the tick values
		mt0 = tf * np.int32(trnge[0]/tf)
		mt1 = tf * (np.int32(trnge[1]/tf) + 1)
		mt = np.arange(mt0,mt1+tf,tf)
		use = np.where((mt >= trnge[0]) & ( mt <= trnge[1]))[0]
		mt = mt[use]		
	print(mt)
	
	#work out the tick labels
	n = mt.size
	hh,mm,ss,ms = DectoHHMM(mt % 24.0)
	print('here')
	utstr = np.zeros(n,dtype='object')
	for i in range(0,n):
		if Seconds:
			utstr[i] = '{:02n}:{:02n}:{:02n}'.format(hh[i],mm[i],ss[i])
		else:
			if ss[i] >= 30:
				mm[i]+=1
				ss[i] = 0
			if mm[i] > 59:
				hh[i]+=1
				mm[i] = 0
			if hh[i] > 23:
				hh[i] = 0
			utstr[i] = '{:02n}:{:02n}'.format(hh[i],mm[i])		
	
	if ShowDate:
		Months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
		labels = np.zeros(n,dtype='object')
		d,t = ContUTtoDate(mt)
		yr,mn,dy = DateSplit(d)
		for i in range(0,n):
			datestr = '{:02d} '.format(np.int(dy[i]))+Months[mn[i]-1]
			if IncludeYear:
				datestr += '\n{:04d}'.format(yr[i])
			labels[i] = utstr[i] + '\n' + datestr			
		
	else:
		#here we just want hh:mm(:ss)
		labels = utstr
		
	#check all of the new labels are within the limits of the plot
	use = np.where((mt >= trnge[0]) & (mt <= trnge[1]))[0]
	mt = mt[use]
	labels = labels[use]
	
	#now convert things back
	trnge -= dt
	tlen -= dt
	mt -= dt	
	if ConvTime:
		trnge *= 3600.0
		tlen *= 3600.0
		mt *= 3600.0

	#now set the ticks/labels
	ax.set_xticks(mt)
	ax.set_xticklabels(labels)
