print("This will convert the entered number into bin!!!")

n = int(input("Enter the number: "))
b = ""
if n == 0:
    print(0)
else:
    while n>0:
        b = b+ str(n%2)
        n//=2   
             

print(b[::-1])

