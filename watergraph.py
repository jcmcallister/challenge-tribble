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
# fx = (3,4,5,7,7,3,2,3,4,6,5,1,0,5)
# fx = (5,1,5) # WORKS! 1 valley, should yield 4
# fx = (5,1,5,3,0,3) # WORKS! multi peaks should yield 7
# fx = (1,1,4,1,0) # WORKS! just one peak, vol == 0
# fx = (1,1) # WORKS! vol == 0
# fx = (1,2,3,0,3,1,0) # WORKS! mountain with a crater on top, vol == 3
fx = (1,2,3,0,3,1,0,5) # max at END, 2 valleys, vol should be 8
# fx = (4,1,6) # WORKS! 1 valley, max at position 0, vol == 3
# fx = (2,1,3) # WORKS! 1 valley, max at end, vol == 1

peaks = []
i=0
currMax = -1
waterVolume = 0

while i < len(fx):
	# print "fx[%d]\t: %d" % (i, fx[i])

	# update max
	if fx[i] > currMax:
		currMax = fx[i]
		# if we update max, we should also update the volume between all spaces
		# 	where there is growth (after a peak -> shrink)

	# if we can peek at next
	if i < (len(fx) - 1):

		# if next is growing
		if fx[i+1] >= fx[i]:
			print "\tGROW from %d to %d!" % (fx[i], fx[i+1])
			# print 'g'

			# if we're growing out of a slump!
			if currMax >= 0:
				waterVolume += min(currMax,fx[i+1]) - (y_interval * fx[i])
				print '\tadding %d water!' % (min(currMax,fx[i+1]) - (y_interval * fx[i]) )

		elif fx[i+1] < fx[i]:

			# next is sinking!

			# we need an addition here in one special case
			
			# print "\tSINK from %d to %d!" % (fx[i], fx[i+1])
			peaks.append(i)
	else:
		# in the last case that the max is the LAST elem
		if currMax == fx[i]:
			waterVolume += currMax - (y_interval * fx[i])
	i += 1;

# print "the max of the values is %d" % currMax
print peaks

print "water volume is %d" % waterVolume

# get min of j & j+1, calculate volume of all f[x] between these indices & add to total
# waterVolume = 0
# maxpeak = -1
# minvalley = 2**16
# for j in peaks:
# 	curr = fx[j]
# 	nxt = fx[j+1]

# 	if curr > maxpeak:
# 		maxpeak = curr


# 	if curr < minvalley:
# 		minvalley = curr

	#look at all indices between maxpeak and minvalley



"""

breakdown

	approach 1: growth-based
		get next # see if we're still growing
		if next < curr, curr is a peak that is now descending
		record curr as a peak in a list


		DIVERGING IDEAS
			1: only record the peaks, then do another pass to get the depths

			2: calculate the a total volume per iteration based on growth/depth

		Idea 1 sounds like it would be easier for devs to follow, costing us 1*O(n)
			no big deal, i guess

		what if instead we had a list of 

"""