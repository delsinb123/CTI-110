#Delsin Barrett
#9/23/2024
#P4HW1
#Use a loop to add valid grades to a list

#create an empty list
grade_list = []


#Get the number of scores that user wants to enter
num_scores = int(input("How many scores do you want to enter? "))

#For loop to get the values of the scores
for score in range(num_scores):
    grade = int(input(f"Enter score #{score+1}: "))


    #If the grade is INVALID, go into the y loop
    while grade <0 or grade >100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        grade = int(input(f"Enter score #{score + 1} again: "))
    #While loop breaks, grade is valid, add it to the list
    grade_list.append(grade)

#All loops are broken
print(f"The valid grades are: {grade_list}")
print(f"The lowest grade is: {min(grade_list)}")

#remove lowest grade from the list
grade_list.remove(min(grade_list))
print(f"The final grades are: {grade_list}")
