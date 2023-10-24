print("Welcome! Let's Find Out Your Percentage(%)")
subs = int(input("Enter the number of subjects you have: "))
m_marks = int(input("Enter the maximum marks in each subject: "))
t_marks = 0
for i in range(subs):
    marks = int(input(f"Enter the marks of Subject {i+1}."))
    t_marks += marks

percent = (t_marks/(subs*m_marks))*100

if percent >= 50:
    print(f"You got {round(percent, 2)}%, Congrats! You have passed the exam")
else:
    print(f"You got {round(percent, 2)}%, Sorry! You failed!, Try again and study hard this year!")
