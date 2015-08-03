def computepay(h,r):
    if h>40:
    	pay = 40*r + (h-40)*1.5*r
    else:
    	pay = h*r  
    return pay

try:
    
	hrs = raw_input("Enter Hours:")
	rph = raw_input("Enter Rate: ")
	hours = float(hrs)
	rate = float(rph)
except:
    print 'Enter numbers'
    quit()
    
p = computepay(hours,rate)

print p