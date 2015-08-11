from math import sqrt, floor

print "------------------------------\nDOUBLE SQUARES CHALLENGE, HIYOOOOO\n"

# nums = (12,4,6,25) # a random tuple appears!
nums = (12,4,6,25,78,3,2,5,7,545678,76567,89,8, 200, 225, 500, 10000)
combos = []

i = 0
numDS = 0
while i < len(nums):
	current = nums[i]

	if current == 0:
		print "0 = 0^2 + 0^2"
	elif current == 1:
		print "1 = 1^2 + 0^2"
	else:
		sqroot = sqrt(current)
		flr = floor(sqroot)
		print "sqrt(%d) is %g which has floor %g" % (current, sqroot, flr)

		if (flr - sqroot) == 0:
			print "\tFOUND - %d == %d^2 + 0^2" % ( current, flr );
			numDS += 1;
			flr -= 1;

		for x in xrange(1, int(flr)+1):

			diff = current - x**2

			if (sqrt(diff) - floor(sqrt(diff)) ) == 0:
				# if both x and floor(sqrt(diff)) are not in combos
				search = "%d-%g"  % ( x, floor(sqrt(diff)) )
				# print "looking for '%s'" % search
				# print combos
				if (not combos) or not (search in combos) :
					print "\tFOUND - %d == %d^2 + %d^2" % (current, x, (floor(sqrt(diff))) );
					combos.append( "%d-%g"  % ( x, floor(sqrt(diff)) ) )
					combos.append( "%g-%d"  % ( floor(sqrt(diff)), x ) )	
					numDS += 1
			elif diff == x**2:
				# if both x and floor(sqrt(diff)) are not in combos
				search = "%d-%d"  % ( x, x )
				# print "looking for '%s'" % search
				if (not combos) or not (search in combos) :
					print "\tFOUND - %d == %d^2 + %d^2" % (current, x, x );
					combos.append( "%d-%d"  % ( x, x ) )
					numDS += 1
	if numDS > 0:
		print "\t%d Double Squares found!\n" % numDS
	i+=1
	numDS = 0
	combos = []		

print "------------------------------\n"