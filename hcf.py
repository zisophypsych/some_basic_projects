print("Welcome! This will find HCF of two numbers!")

num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))

if num_1 == num_2:
    print(f"HCF of {num_1} and {num_2} is {num_1}")
elif num_1 < num_2:
    while True:
        if num_2 % num_1 == 0:
            print(f"HCF of {num_1} and {num_2} is {num_1}")
            break
        else:
            num_2 = num_1
            num_1 = num2 % num_1
else:
    while True:
        if num_1 % num_2 == 0:
            print(f"HCF of {num_1} and {num_2} is {num_1}")
            break
        else:
            num_1 = num_2
            num_2 = num_1 % num_2


            
     
