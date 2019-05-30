def reverse(message):
	i=0
	word=""
	while i<len(message):
		if msg==" ":
			word+=1
			i=len(word)-1
			while word>=1:
				print (word)
				word=""
			i=i-1
		else word=message[i]+word
	i+=1
msg=input("Enter a message: ")
reverse(msg)


