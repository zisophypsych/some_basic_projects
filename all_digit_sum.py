print("Welcome! Let's add all the digits of the number!")
num = str(input("Enter The Number: "))

yog = 0
for i in num:
    yog += int(i)

print("Sum of all the digits of the given number is:", yog)
