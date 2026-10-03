# Write a program to input two numbers and print which one is greater. If both are equal, print that they are equal.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1>num2:
    print(f" {num1} is greatest Number.")
elif num1<num2:
    print(f"{num2} is greatest number")
else:
    print("Both are equal")