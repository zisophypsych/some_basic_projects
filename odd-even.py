print("Welcome! This will check if the number is odd or even!")
num = float(input("Enter the number: "))
two = num%2
if two == 0:
    print(f"{int(num)} is a Even Number")
elif two == 1:
    print(f"{int(num)} is a Odd Number")
else:
    print("Noninteger ERROR!, careful next time")
