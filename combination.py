msg=input("Enter any message: ")
what=input ("What are you looking for? ")
i=0
count=0
while i+len(what)<=len(msg):
	if msg[i:i+len(what)]==what:
		count=count+1
	i=i+1
print (count)