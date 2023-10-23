while True:
    choice = int(input("Welcome! Enter 1 for PRODUCT(*) Or Enter 2 for ADDITION(+) , For Two Numbers, and 3 for EXIT! :  "))
        
    if choice == 3:
        print("Thanks For Using!!")
        break
    elif choice != 1 and choice != 2:
        print("Wrong Input!! Only Enter 1, 2 & 3")
    else:
        First_num = int(input("Enter First Number: "))
        Second_num = int(input("Enter Second Number: "))

        if choice == 2:
            sumo = First_num + Second_num
            print(f"Sum of two numbers is {sumo}")
        elif choice == 1:
            prod = First_num * Second_num
            print(f"Product of two numbers is {prod}")
        else:
            print("Something Went Wrong!!")





   


