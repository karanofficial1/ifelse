"""
Write a program to input marks and assign grades based on the following conditions:
• 90 and above → Grade A
• 80 and above → Grade B
• 70 and above → Grade C
• 60 and above → Grade D
• Below 60 → Fail
"""

marks = int(input("Enter your marks: "))

if marks >=90 and marks <=100:
    print("Grade A")
elif marks >=80 and marks <90:
    print("Grade B")
elif marks >=70 and marks <80:
    print("Grade C")
elif marks >=60 and marks <70:
    print("Grade D")
elif marks >=0 and marks <= 59:
    print("Fail")
else:
    print("Plz Check your marks")