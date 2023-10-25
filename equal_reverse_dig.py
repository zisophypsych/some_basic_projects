print("Welcome! Let's find out whether reverse of the number will be equal or not! ")

num = str(input("Enter the number: "))
n_num = str()
for i in range(len(num)-1, -1,-1):
    n_num += num[i]

if int(num) == int(n_num):
    print(f"{num} and its reverse {n_num} is equal!")
else:
    print(f"{num} and its reverse {n_num} is not equal!")


