alpha=input("Enter a character: ")
if ord(alpha)>=65 and ord(alpha)<=90:
	print ("This is an upper case letter.")
else:
	if ord(alpha)>=97 and ord(alpha)<=122:
		print ("This is a lower case letter.")
	else: 
		if ord(alpha)>=48 and ord(alpha)<=57:
			print ("This a value between 0 and 9.")
		else: 
			print ("This is any other character.")