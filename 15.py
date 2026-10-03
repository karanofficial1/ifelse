# Write a program to input three numbers and print the largest among them.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1>num2 and num1>num3:
    print("First no. is greatest number: ", num1)
elif num2>num1 and num2>num3:
    print("second no. is greatest number: ", num2)
elif num3>num1 and num3>num2:
    print("Third no. is greatest number: ", num3)
else:
    print("All Number are equal.")



# if num1>num2:
#     if num1> num3:
#         print("First number is greatest number: ", num1)
#     else:
#         print(" Third no. is greatest Number: ", num3)
# elif num2>num1:
#     if num2>num3:
#         print("Second no. is greatest number. ", num2)
#     else:
#         print("Third number is greatest number. ", num3)
# elif num3>num1:
#     if num3>num2:
#         print("Third number is greatest number- ", num3)
#     else:
#         print("Second no. is greatest number- ", num2)
# else:
#     print("All number are equal")