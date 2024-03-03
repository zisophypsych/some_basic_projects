print("THis will count the digits of the Entered number: ")

n = int(input("Enter the number: "))
#print(len(str(n)))
d = 0
while n>0:
    n//=10
    d+=1
print(d)
