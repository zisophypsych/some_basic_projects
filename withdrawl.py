print("Welcome to the ATM !")
am = int(input("Enter the amount for withdrawal Rs. "))
hund = am//100
am -= hund*100
fifty = am//50
am -= fifty*50
ten = am//10 
am -= ten*10
if am != 0:
    print 

print(f"Please Collect {hund} Hundred Rupee , {fifty} Fifty Rupee And {ten} Ten Rupee Notes ")
if am != 0:
    print(f"!!We don't have notes or coins below Rs.10 , Sorry We can't give you Rs.{am}")
    
