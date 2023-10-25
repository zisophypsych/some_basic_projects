print("Welcome! Let's Find Out Your Percentage(%) And Division")
subs = int(input("Enter the number of subjects you have: "))
m_marks = int(input("Enter the maximum marks in each subject: "))
t_marks = 0
for i in range(subs):
    marks = int(input(f"Enter the marks of Subject {i+1}."))
    if marks <= m_marks:
        t_marks += marks
    else:
        print("Wrong input, Try again!")
        break

percent = (t_marks/(subs*m_marks))*100

if percent >= 60:
    print(f"You have {round(percent, 2)}%, Congrats! You got First Division!")
elif percent >= 50 and percent <= 59:
    print(f"You have {round(percent, 2)}%, Congrats! You got Second Division!")
elif percent >= 40 and percent <= 49:
    print(f"You have {round(percent, 2)}%, Congrats! You got Third Division!")
else:
    print(f"You have {round(percent, 2)}%, Sorry! You failed this year!")
