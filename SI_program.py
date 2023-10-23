print("Welcome!, Lets find the Simple Interest for your Loan\n")
principle_amount = int(input("Enter the Principle Amount : Rs."))
time_period = int(input("Enter the time period in years : "))
rate = int(input("Enter the Interest Rate(%) of the Loan : "))
#print("\n")

simple_interest = (principle_amount*time_period*rate)/100

print(f"Simple Interest for your Loan will be : {simple_interest} Rs.")
