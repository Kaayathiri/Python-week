product = input ("enter a product:")
price = input ("enter the price:")
qty = input ("enter a quantity: ")
amount =  float(price) * int(qty)
VAT = amount * 15/100
Bill = amount + VAT
print ("Your receipt:", Bill)
print ("Product:", product)
print ("Amount of the product:", amount)
print ("VAT of product:", VAT)
