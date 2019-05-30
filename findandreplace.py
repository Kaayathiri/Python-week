file_read=open("data.txt","r")
file_write=open("data2.txt","w")
def replace(message, text, start, end):
	newmessage=""
	if not start==0:
		newmessage+= message[0:start]
	newmessage+=text
	if not end==len(message)-1:
		newmessage+=message[end+1:len(message)]
	return newmessage



def findandreplace(text,find,newword):
	lenfind=len(find)
	lentext=len(text)
	i=0
	while i+lenfind<lentext:
		if text[i:i+lenfind]==find:
			text1=text
			replace1=newword
			startingindex=i
			endingindex=i+lenfind-1
			text2=replace(text1, replace1, startingindex, endingindex)
			text=text2
		i+=1
	return text


for line in file_read:
	line=findandreplace(line,"am","***")
	print (line,file=file_write)






