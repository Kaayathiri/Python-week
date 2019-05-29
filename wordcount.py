def wordcount (message):
	word=1
	i=0
	while i<len(message):
		if message [i]==" ":
			word+=1
		i+=1
	return word 
message1=input ("Enter a message: ")
if wordcount(message1)>1:
	print ("Words:", wordcount(message1))
else:
	print ("Word:", wordcount(message1))