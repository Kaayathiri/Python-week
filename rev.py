

message=input("Enter a message: ")
newmessage=""
word=""
i=0
while i<len(message):
	if message[i]==" ":
		newmessage+=(word+" ")
		word=""
	else: 
		word=message[i]+word
	i=i+1
newmessage+=(word+" ")
print (newmessage)

