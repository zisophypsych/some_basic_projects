print("Welcome! This will tell whether the number is prime or not!")

num = int(input("Enter the number: "))

if num == 0 or num == 1:
    print(f"{num} is not a prime number!")

prime = 0
for i in range(2, int(num/2)+1):
    if (num%i) == 0:
        prime = 1
        break

if prime == 1:
    print(f"{num} is not a prime number!")
else:
    print(f"{num} is a prime number")
        
            
