# Write a program to check if a student gets a scholarship.
# • Scholarship is granted if marks > 85 AND attendance > 75%


marks = int(input("Enter your marks : "))
attendance = float(input("Enter your attendance (Percentage): "))

if marks > 85 and attendance > 75:
    print("Congratulations! You are granted scholarship.")
else:
    print("Sorry! You cannot granted scholarship.")