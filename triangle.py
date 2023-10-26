print("Welcome! Let's find out whether the triangle is valid or not!")

a1 = int(input("Enter 1st Angle of the triangle: "))
a2 = int(input("Enter 2nd Angle of the triangle: "))
a3 = int(input("Enter 3rd Angle of the triangle: "))

if a1+a2+a3 == 180:
    print("Triangle is valid!")
else:
    print("Triangle is not valid!")

