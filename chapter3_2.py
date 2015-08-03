score = raw_input("Enter your score between 0.0 and 1.0: ")
s = float(score)

if s < 0.0:
    print 'score is out of range'
    quit()
    
elif s > 1.0:
    print 'Score is out of range'
    quit()

elif s>=0.9:
	print 'A'
    
elif s>=0.8:
	print 'B'
    
elif s>=0.7:
	print 'C'
    
elif s>=0.6:
	print 'D'
    
else:
	print 'F'