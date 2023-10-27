print("Welcome! This program will print the factorial of any number!")

num = int(input("Enter the number: "))

factorial = 1
for i in range(1, num+1,1):
    factorial *= i

print(f"factorial of {num} is {factorial}")
