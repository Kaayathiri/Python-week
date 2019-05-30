file_read=open("data.txt","r")
file_write=open("data21.txt","w")
for line in file_read:
	for ch in line:
		if ch=="o":
			print ("*",end="",file=file_write)
		else:
			print (ch,end="",file=file_write)
