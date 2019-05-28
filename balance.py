no=input ("Enter no:")
amount = input ("Enter the amount:")
change=int(no)-int(amount)
Fifty=int(change/50)
twenty= int(((change-50*Fifty)%50)/20)
ten=int(((change-20*twenty)%20)/10)
five=int(((change-10*ten)%10)/5)
two=int(((change-5*five)%5)/2)
one=int(((change-2)*two)%2)
print ("Change:",change)
if Fifty>0:
	print ("Fifty:", Fifty)
if twenty>0:
	print ("Twenty:", twenty)
if ten>0:
	print ("Ten:",ten)
if five>0:
	print ("Five:", five)
if two>0:
	print ("Two:", two)
if one>0:
	print ("One:", one)

