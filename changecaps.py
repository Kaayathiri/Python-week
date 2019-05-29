alpha=input("Enter any character: ")
if ord(alpha)>=65 and ord(alpha)<=90:
	print ("This is",chr(ord(alpha)+32))
else: 
	if ord(alpha)>=97 and ord(alpha)<=122:
		print ("This is",chr(ord(alpha)-32))
	else:
		if ord(alpha)>=48 and ord(alpha)<=57:
			print ("This is a number")
		else: 
			print ("This is a special character.")