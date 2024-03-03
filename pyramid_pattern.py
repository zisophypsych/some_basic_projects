print("This will print Pyramid Pattern!!!")

n = int(input("Enter the number: "))

s = 1
for i in range(n):
    print(" "*(n-i-1), end="")
    for j in range(s):
        
        print("*", end = "")
    s+=2
    print()
