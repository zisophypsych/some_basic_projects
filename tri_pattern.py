print("THis will print Triangular Pattern! ")

n = int(input("Enter the number: "))

for i in range(1,n+1):
    for k in range(1,i+1):
        print("*",end=" ")
    print()
