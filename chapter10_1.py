name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

def count(lines,s):
    counts = dict()
    for line in lines:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
	    str = line[5]
	    hour = str[0:str.find(":"):1]
            counts[hour] = counts.get(hour,0) + 1
    return counts

def sort(d):
    lst = list()
    for key, val in d.items():
        lst.append((key,val))
    lst.sort()
    for val,key in lst:
        print val,key
    
dictionary = count(handle,'From')
t = sort(dictionary)