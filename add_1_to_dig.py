print("Welcome! , This program will add 1 to each of the digits of the number you enter!")
num = input("Enter the number: ")
n_num = str()
for i in num:
    n_dig = str(int(i) + 1)
    n_num += n_dig
print(int(n_num))


