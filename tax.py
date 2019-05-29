def tax (salary):
	if salary >1500:
		T=salary*21/100
	else: 
		T=salary*15/100
	return T
salary1=int(input("Enter your salary: "))
print ("Your tax =", tax(salary1))
print ("Your net salary is", (salary1-tax(salary1)))
