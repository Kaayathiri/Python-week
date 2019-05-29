def ones (number):
	result=""
	if number==1:
		result=" One"
	if number == 2:
		result= " Two"
	if number == 3:
		result= " Three"
	if number == 4:
		result= " Four"
	if number == 5:
		result= " Five"
	if number == 6:
		result= " Six"
	if number == 7:
		result= " Seven"
	if number == 8:
		result= " Eight"	
	if number == 9:
		result= " Nine"
	if number == 10:
		result= " Ten"
	if number == 11:
		result= " Eleven"
	if number == 12:
		result= " Twelve"
	if number == 13:
		result= " Thirteen"
	if number == 14:
		result=" Fourteen"
	if number == 15:
		result= " Fifteen"
	if number == 16:
		result= " Sixteen"
	if number == 17:
		result= " Seventeen"	
	if number == 18:
		result= " Eighteen"	
	if number == 19:
		result= " Nineteen"	
	return result

def tens(number):
	result=""
	if number==20:
		result=' Twenty'
	if number==30:
		result=" Thirty"
	if number==40:
		result=" Fourty"
	if number==50:
		result=" Fifty"
	if number==60:
		result=" Sixty"
	if number==70:
		result=" Seventy"
	if number==80:
		result=" Eighty"
	if number==90:
		result=" Ninety"
	return result
num=int(input("Enter any number: "))
answer=""
if num>=1000 and num<=9999:
	answer+=ones(int(num/1000))+" Thousand"
	num=num%1000
if num>=100:
	answer+=ones(int(num/100))+" Hundred"
	num=num%100
if num>=20:
	answer += tens(int(num/10)*10)
	num=num%10
if num>0 and num<=19:
	answer+=ones(num)
print (answer)