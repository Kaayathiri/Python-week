def change(message):
	i=0
	word=""
	while i<len(message):
		if ord(message[i])>=65 and ord(message[i])<=90:
			word+=(chr(ord(message[i])+32))
		else:
			if ord(message[i])>=97 and ord(message[i])<=122:
				word+=(chr(ord(message[i])-32))
			else:
				if ord(message[i])>=48 and ord(message[i])<=57:
					word+=str(int(message[i])*2)
				else:
					word+=chr(ord(message[i]))
		i=i+1
	print(word)
msg=input("Enter a message: ")
change(msg)