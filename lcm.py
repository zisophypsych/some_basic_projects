import math
print("This will give the LCM of the entered numbers!!!")

a = int(input("Enter the first number: "))
b = int(input("ENter the second number: "))
m = max(a,b)

lcm = a*b
for i in range(m,a*b):
    if i%a==0 and i%b==0:
        lcm = i 
        break

print(lcm)
print("lcm through math lib", (a*b)/(math.gcd(a,b)))
