# Extended Leap Year Task — Given a year, return True if it is a leap year, otherwise return False, following the Gregorian
# calendar rules:
# • The year can be evenly divided by 4 → Leap year, unless:
# • The year can be evenly divided by 100 → NOT a leap year, unless:
# • The year is also evenly divisible by 400 → IS a leap year
   

year = int(input("Enter year: "))

if year % 4 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("leap year")
elif year % 400 == 0:
    print("not leap year")
else: 
    print("Not leap year")