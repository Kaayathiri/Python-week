file_read=open("data.txt","r")
file_write=open("data21.txt","w")
for line in file_read:
	for ch in line:
		if ch=="a":
			print ("**",end="")
			if ch=="m":
				print ("*",end="")
		else:
			print (ch,end="")
			