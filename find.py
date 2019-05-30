find=input("What are you looking for: ")
replace=input("Replace with what: ")
F_read=open("data.txt","r")
F_write=open("data22.txt","w")
for data in F_read:
	i=0
	while i<len(data):
		if data[i]==find[0]:
			if data[i:len(find)+1]==find:
				print (replace,end="",file=F_write)
				i+=len(find)-1
			else:
				print(data[i],end="",file=F_write)
		else:
			print(data[i], end="",file=F_write)
		i=i+1
