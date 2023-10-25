print("Welcome! Let's Find Out You are insured or not!\n")

marital_s = int(input("Marital Status , Enter 1 if you're married and 0 if you're unmarried: "))
sex = int(input("Sex, Enter 1 for male and 2 for female: "))
age = int(input("Enter Your Age: "))

if marital_s == 1:
    print("Congrats! Company will cover your insurance!")
elif sex == 1 and age > 30:
    print("Congrats! Company will cover your insurance!")
elif sex == 2 and age > 25: 
    print("Congrats! Company will cover your insurance!")
else:
    print("Sorry! Company can't cover Your Insurance")
