print("Welcome! This will print Fibonacci Series!")

terms = int(input("Enter how many terms you want in Series: "))
series = []
for i in range(terms):
    if i == 0:
        series.append(0)
    elif i == 1:
        series.append(1)
    else:
        termN = series[(i-1)]+series[(i-2)]
        series.append(termN)

print(series)


