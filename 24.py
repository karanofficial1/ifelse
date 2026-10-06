# Write a program to check whether a given year is a leap year.
# • Divisible by 4 → Leap year, UNLESS:
# • Divisible by 100 → NOT a leap year, UNLESS:
# • Also divisible by 400 → IS a leap year


year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else: 
        print("not leap year")
else: 
    print("Not leap year.")