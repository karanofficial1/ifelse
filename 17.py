# Write a program that takes three sides of a triangle and checks whether the sides can form a valid triangle.

side1 = float(input("Enter the length of first side of triangle: "))
side2 = float(input("Enter the length of second side of triangle: "))
side3 = float(input("Enter the length of third side of triangle: "))

if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print("It is valid triangle.")

else:
    print("Invalid triangle.")