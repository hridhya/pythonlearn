name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read()
words = text.split()

#print words


dic = {}
i = 0
for word in words:
    i=i+1
    if word.startswith("From:"):
        dic[words[i]] = dic.get(words[i],0)+1
        
        
bigcount = None
email = None
for key,value in dic.items():
    if bigcount==None or bigcount<value:
        bigcount = value
        email = key

print email, bigcount