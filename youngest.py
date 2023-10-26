print("Welcome! Let's Find Out Who is the youngest")
print("This software has the assumption that all the three people have different age!")
ram = int(input("Enter Ram's Age: "))
shyam = int(input("Enter Shyam's Age: "))
ajay = int(input("Enter Ajay's Age: "))


if ram < shyam and ram < ajay:
    print("Ram is the youngest of three!")
elif shyam < ram and shyam < ajay:
    print("Shyam is the youngest of three")
else:
    print("Ajay is the youngest of three!")
