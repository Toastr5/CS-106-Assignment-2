Lname = input("Enter your last name: ")
midterm = float(input("Enter your numerical midterm score: "))
final_exam = float(input("Enter your numerical final exam score: "))
#calcuations
total_score = midterm * 0.4 + final_exam * 0.6
print (f"{Lname} your total exam points are {total_score}")
