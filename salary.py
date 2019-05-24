name= input ("Enter your name:")
salary= int(input("Enter your salary:"))
if salary>2000:
	tax=salary*25/100
else:
	tax=salary*15/100
netsalary=salary-tax
print ("Your name:",name)
print ("Your salary:",salary)
print ("Your tax:", tax)
print ("Your netsalary:", netsalary)
