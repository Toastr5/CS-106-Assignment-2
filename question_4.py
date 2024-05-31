make = input(str("Enter the make of the car: "))
model = input(str("Enter the model of the car: "))
msrp = input(str("Enter the MSRP of the car: "))
discount = float(input("Enter the discount percentage in decimal form: "))
discount_percent = discount * 100
#calcuations
ammount_off = float(msrp) * float(discount)
discounted_price = float(msrp) - float(ammount_off)
print(
  F"The {make} {model} costs {discounted_price}" 
  F" dollars after the {discount_percent} percent discount.")