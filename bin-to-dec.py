print("This will convert the entered binary into decimal!!")

n = int(input("Enter the Binary Number: "))

dec = 0
for i in range(0,len(str(n)),-1):
    if int(str(n)[i])==0:
        dec+=0
    elif int(str(n)[i])==1:
        dec+=(2**(len(str(n)-1-i))) 
    else:
        print("Invalid input !! Enter Binary Only!!!")

print(dec)

    


