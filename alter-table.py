print("Welcome! THis will print table but alternate multiples!")

num = int(input("Enter the number: "))

for i in range(1,11,2):
    print(f"{num} * {i} = {num*i}")
