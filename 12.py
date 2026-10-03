# Write a program where if the total shopping bill is greater than 1000, apply a 10% discount and print the final amount.

amount = float(input("Enter the bill amount: "))
total= 0

if amount > 1000:
    total = amount - amount * 0.1
    print("Your bill amount after discount is: ", total)
else:
    print("your bill amount is :", amount)
