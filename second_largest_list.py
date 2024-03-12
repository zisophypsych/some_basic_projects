print("This will print the second largest element of the Entered List!!!\n")
i = int(input("Enter the number of elements you want in your list: "))
l = []
j = 0
while j < i:
    e = int(input("\nEnter the elements one by one !!Only Numbers!! => "))
    l.append(e)
    j+=1

l.sort()
print(l[-2])

