# Write a program to validate a login system. If username is 'admin' and password is '1234', print 'Login Successful', else print
# 'Invalid Credentials'.

username = input("Enter your username: ").lower()
password = input("Enter your password")

if username == "admin" and password == "1234":
    print("Login Successful. Welcome to our page")
else:
    print("Invalid Credentials.")