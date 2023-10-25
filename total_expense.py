print("Welcome! Let's find out your total expenditure!\n")
print("SPECIAL OFFER! 10% DISCOUNT IF THE QUANTITY IS ABOVE 1000!")

price = int(input("Enter price per item: "))
quant = int(input("Enter quantity: "))
total = price*quant

if quant >= 1000:
    print(f"Congrats! You got 10% OFF, and your total expense will be Rs.{(90/100)*total}")
else:
    print("Your total expense will be Rs.", total)
