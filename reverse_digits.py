print("Welcome! Let's Reverse the digits of your number!")
num = str(input("Enter the Number: "))
n_num = str()
for i in range(len(num)-1, -1, -1):
    n_num += num[i]

print(n_num)
