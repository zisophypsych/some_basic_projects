print("This will print the Entered text n times using RECURSION!!!!")

t = input("Enter the text: ")
n = int(input("Enter n: "))

def PrintNTimes(n):
    print(t)
    if n > 1:
        PrintNTimes(n-1)

PrintNTimes(n)

