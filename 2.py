# Write a program that asks the user for their age and prints whether they are eligible to vote (18 years or older).

age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
else:
    print("not eligible to vote.")