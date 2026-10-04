# Write a program to give a movie ticket discount:
# • Age < 12 or Age > 60 → Discount applies
# • Otherwise → No discount

age = int(input("Enter your age: "))

if age < 12 or age > 60:
    print("Congratulations! You will get Discount.")
else:
    print("Sorry! No Discount.")