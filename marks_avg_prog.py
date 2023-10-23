print("Welcome! , Let's find out the Average, Sum and Percentage(%) Of your Subjects marks\n")
num_subs = int(input("Enter the number of subjects you have: ")) 
max_marks = int(input("Enter the maximum marks in Each subject : "))
total_marks = 0
for i in range(num_subs):
    obt_marks = int(input(f"Enter the Marks of subject {i+1}. "))
    total_marks += obt_marks

avg = total_marks/num_subs
max_all = max_marks*num_subs
percent = (total_marks/max_all)*100

print(f"Sum of all your Marks is {total_marks} ")
print(f"Average of your Marks is {avg}")
print(f"Your Percentage is {percent}")
