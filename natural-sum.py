print("Welcome! This program will add all the natural numbers till the number you enter!")

num = int(input("Enter the number: "))

yog = 0
for i in range(1, num+1,1):
    yog += i 

print(f"Sum of all the natural numbers till {num} is {yog}")
