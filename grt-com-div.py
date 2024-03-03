print("This will print the Greatest Common divisor between entered 2 numbers!!!")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
s = min(a,b)

gcd = 1
for i in range(s,1,-1):
    if b%i==0 and a%i==0:
        gcd = i 
        break
print(gcd)
