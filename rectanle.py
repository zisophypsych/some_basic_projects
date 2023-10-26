print("Welcome! Let's find whether the area of rectangle is greater than its perimeter or not!")
print("NOTE! Enter Length and breadth in cm only!!!")
l = int(input("Enter the Length of the Rectangle: "))
b = int(input("Enter the breadth of the Rectangle: "))

area = l*b 
perimeter = 2*(l+b)

if area < perimeter:
    print(f"Area = {area} cm square, Perimeter = {perimeter} cm And Perimeter is greater than Area!")
else:
    print(f"Area = {area} cm square, Perimeter = {perimeter} cm And Area is greater than Perimeter!")
