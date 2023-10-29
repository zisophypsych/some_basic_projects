print("Welcome! This is gonna check whether a number is Palinrome or not!")

num = str(input("Enter the number: "))
n_num = str()
for i in range(len(num)-1, -1, -1):
    n_num += num[i]

if int(num) == int(n_num):
    print(f"Hurray! {num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
