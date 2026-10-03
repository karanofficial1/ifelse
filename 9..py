# Write a program to validate whether an email ends with '@gmail.com'.


# string = input("Enter your gmail address: ")
# new = string.split("@")

# if new[1] == "gmail.com":
#     print("Valid gmail address")
# else:
#     print("NOt valid gmail address")

string = input("Enter your gmail address: ")
new = string.find("@")

if string[new::] == "@gmail.com":
    print("Valid gmail address")
else:
    print("NOt valid gmail address")