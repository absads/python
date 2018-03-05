for n in range(2, 10): 		# total range of numbers
	isDiv = False
	for x in range(2, n): 	# get numbers less than n
		if n % x == 0: 	# check modulo
			print n, '=', x, '*', n/x
			isDiv = True
			break
	# Check whether isDiv is True or False
	if not isDiv:
		print n, 'Prime number'
