# Delsin Barrett
# 9/11/2024
# P1HW2
#Use if/elif/else statements with a variable

#User inputs grades
module1 = float(input("Enter your grade for Module 1: "))
module2 = float(input("Enter your grade for Module 2: "))
module3 = float(input("Enter your grade for Module 3: "))
module4 = float(input("Enter your grade for Module 4: "))
module5 = float(input("Enter your grade for Module 5: "))
module6 = float(input("Enter your grade for Module 6: "))

#Calculate Grades
lowest = min(module1, module2, module3, module4, module5, module6)
highest = max(module1, module2, module3, module4, module5, module6)
sum_of_grades = module1 + module2 + module3 + module4 + module5 + module6
average = sum_of_grades/6

#Print Results
print("------------Results------------")
print("Lowest Grade:      ", lowest)
print("Highest Grade:     ", highest)
print("Sum of Grades:     ", sum_of_grades)
print("Average:           ", average)

#Determine Letter Grade
if average >= 90:
    letter_grade="A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade="C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print("---------------------------------------")
print("Your grade is:", letter_grade)
