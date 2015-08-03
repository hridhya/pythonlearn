fname = raw_input("Enter file name: ")
fh=open(fname)

count = 0
sum = 0


for line in fh:

    
    if line.strip().startswith('X-DSPAM-Confidence'):
		value = line.find(':')
		flt = float(line[value+1:])
		count = count+1
		sum = sum+flt

average = sum/count

print "Average spam confidence:",average

