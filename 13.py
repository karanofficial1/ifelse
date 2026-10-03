''' 
Write a Python program to create a simple calculator that takes two numbers (num1 and num2) and an operator (+, −, ×, ÷)
as input from the user. Perform the corresponding operation based on the given operator using elif statements
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

symbol = input("Enter +, -, *  or / ")

if symbol =="+":
    print(f" The sum of {num1} and {num2} is :", num1 + num2)
elif symbol == "-":
    print("The subtraction of {} - {} is {}".format(num1, num2, num1-num2))
elif symbol == "*":
    print("The multiplication of {} * {} is {}".format(num1, num2, num1*num2))   
elif symbol == "/":
    print("The division of {} / {} is {}".format(num1, num2, num1/num2))
else:
    print("You entered a wrong symbol.")