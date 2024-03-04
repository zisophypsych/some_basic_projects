import sys
print("This will prime the prime factorisation of the entered number!!!")

n = int(input("Enter the number: "))

l = []

if n==0 or n==1:
    print("Invalid Input!!! Pls enter number that is greater than 0 and 1.!!")
    sys.exit()


while n%2==0:
    l.append(2)
    n//=2

for i in range(3,n,2):
    if n%i==0:
        while n%i==0:
            l.append(i)
            n//=i 

if n>1:
    l.append(n)

print(l)
#for j in l:
#print(j,end="*")
