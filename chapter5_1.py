largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done" : 
		break
	try:
		n = int(num)
		if largest == None:
			largest = n
		if smallest == None:
			smallest = n
		if n > largest:
			largest = n
		if n < smallest:
			smallest = n
	except:
		print 'Invalid input'
        continue

print "Maximum is", largest
print "Minimum is", smallest