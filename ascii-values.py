print("Welcome! Let's find whether the character entered is capital letter, small letter, a digit or a special symbol!")

c = input("Enter the character: ")
a_code = ord(c) 

if a_code >= 65 and a_code <= 90:
    print(f"{c} is a capital letter!")
elif a_code >= 97 and a_code <= 122:
    print(f"{c} is a small letter!")
elif a_code >= 48 and a_code <= 57:
    print(f"{c} is a Digit!")
elif a_code <= 127:
    print(f"{c} is a special symbol!")
