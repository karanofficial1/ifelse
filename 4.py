# Write a program to input a character and check whether it is a vowel (a, e, i, o, u) or a consonant
character = input("Enter a character: ")

if len(character) != 1:
    print("Enter one character only.")
elif character.isdigit:
    print("Its number. Plz reenter the word")
elif character =="a" or  character =="e" or character =="i" or character =="o" or character =="u":
    print("It is vowel.")

else:
    print("it is consonent")