print("This will print the Inverted Triangle!!!")
n= int(input("Enter the number: "))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*", end = " ")
    print()
