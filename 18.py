# Write a program that calculates an electricity bill based on units consumed:
# • Units ≤ 100 : Rate = Rs. 5 per unit
# • Units 101 – 200 : Rate = Rs. 7 per unit
# • Units > 200 : Rate = Rs. 10 per unit


unit = int(input("Enter your units consumed: "))
if unit <= 100:
    print("Your Bill amount is :", unit * 5)

elif unit >=101 and unit <=200:
    print("Your Bill amount is: ", unit * 7 )

else:
    print("Your Bill amount is: ", unit * 10 )