try:
	no1=int(input("Enter the first number: "))
	no2=int(input("Enter the second number: "))
	result=no1/no2
	print("The result is", result)
except ValueError:
	print ("Please print a number ")
except ZeroDivisionError:
	print ("Cannot divide a value by zero")
finally: print("This is the answer")