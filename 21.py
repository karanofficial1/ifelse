# Write a program to check whether a given year is a century year (year ends with 00).

year = int(input("Enter the year: "))

if year % 100 == 0:
    print("century year.")

else:
    print("not century year.")