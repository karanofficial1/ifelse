# Write a program to determine employee bonus:
# • Bonus is awarded only if experience > 2 years AND performance rating > 7

exp = int(input("Enter your experience: "))
rating = int(input("Enter your performance rating: "))

if exp > 2 and rating > 7:
    print("Congratulations You will get Bonus.")

else:
    print("Sorry! Do hard labour.")