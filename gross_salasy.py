print("Welcome! Let's Calculate Your Dearness Allowance(40%) , House Rent Allowance(20%) And Gross Salary!")

bas_sal = int(input("Enter your basic salary Rs. "))
da = bas_sal*(40/100)
hra = bas_sal*(20/100)

print(f"Your Dearness Allowance is Rs.{da} , Your House Rent Allowance is Rs.{hra}, And Your Gross Salary is Rs.{bas_sal+da+hra}")


