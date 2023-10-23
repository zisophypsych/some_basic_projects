print("Welcome! Let's Find out the Area of Circle and Rectangle!\n")
print("NOTE : The unit we use here is 'cm', So please make sure all your measurments will be in cm.\n")

while True: 
    choice = int(input("Enter 1 to find the area of circle , 2 for Rectangle and 3 for Exit!: "))
    if choice == 1:
        r = int(input("Enter the Radius of the circle in cm: "))
        ar_cir = 3.14*(r**2)
        print(f"Considering PI = 3.14, Area of the circle is {ar_cir} cm square")
    elif choice  == 2:
        l = int(input("Enter the length of the Rectangle in cm: "))
        b = int(input("Enter the breadth of the Rectangle in cm: "))
        print(f"Area Of the Rectangle is {l*b} cm square")
    elif choice == 3:
        print("Thanks for using !!")
        break
    else:
        print("Wrong Input!, Try Again!")
