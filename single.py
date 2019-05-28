msg= input ("Enter any message: ")
character = input ("What are you looking for? ")
i=0
count=0
while i<len(msg):
	if msg[i]==character:
		count=count+1
	i=i+1
if count>1:
	print ("There are", count,"letters")
elif count==0:
	print ("There are no letters")
else:
	print ("There is only", count, "letter" )


