print("This will print the next Prime number from the entered NUmber!!!")

n = int(input("Enter the number: "))

while True:
    n+=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        print(n)
        break

