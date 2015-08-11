# Water inside a bar graph

"""	given any bar graph and it's axes intervals, find out how much water you could fit
	 inside any complete valleys (not including "runoff" down any steep sides)
	 """

"""thoughts:
		do an O(n) loop over the graph's x values, looking at y(x) per point
			record all potential valley peaks by matching
				if all points between points y1 and y2 are less than y1 and y2
					you have a valley!
					record the valley's peaks in a list

			run over the list of valley peaks and get all y(x) points between x2-x1
				do basic rectangle products & addition
					(given any low point p between the min of x2/x1 values)
						we assume that any water contained in a valley above this min(x1,x2) "runs off"
					waterDepthTotal += y( min(x2,x1) ) - p for every low point p between 2 peaks


"""

x_interval = 1
y_interval = 1
fx = (3,4,5,7,7,3,2,3,4,6,5,1,0,5)
peaks = []
lastpeaklocation = 0
currMax = -999
i=0

while i < len(fx):
	print "fx[%d]\t: %d" % (i, fx[i])

	if currMax < fx[i]:
		currMax = fx[i];

	# get a peak list
	if lastpeaklocation == 0:
		# leftpeaks.append(fx[i]);
		leftpeak = fx[i]

	# if we can peek at next
	if i < (len(fx) - 1):

		# if next is growing
		if fx[i+1] > fx[i]:
			print "\tGROW from %d to %d!" % (fx[i], fx[i+1])
			lastpeaklocation = i+1;
		
			# we reset the peak to the next one, which is higher
			leftpeak = fx[i+1]

			# were we in a valley just now? if so, add locations to the valley list



		elif fx[i+1] < fx[i]:

			# next is shrinking!

			print "\tSHRINK from %d to %d!" % (fx[i], fx[i+1])

			# was there a leftpeak to match this peak? if so, calc the water depth

			lastpeaklocation = i;

		peaks.append(lastpeaklocation)

	i += 1;

print "the max of the values is %d" % currMax
print peaks