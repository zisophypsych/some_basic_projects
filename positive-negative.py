print("Welcome! This program will check whether the numbers are postive, negative or zero!")

num = int(input("How many numbers you want to check?: "))

n_list = []

for i in range(num):
    n = int(input(f"Enter number {i+1}."))
    n_list.append(n)

for i in n_list:
    if i == 0:
        print(f"{i} is a zero!")
    elif i < 0:
        print(f"{i} is a negative number!")
    else:
        print(f"{i} is a postive number!")


