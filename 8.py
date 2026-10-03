# Write a program to check whether a string entered by the user is a palindrome (same forward and backward).

string = input("Enter your string: ")
if string == string[::-1] :
    print("Palindrome")
else:
    print("Not Palindrome")