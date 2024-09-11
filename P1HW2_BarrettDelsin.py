# Delsin Barrett
# 9/11/2024
# P1HW2
#create program on IDLE

print("This program calculates and displays travel epenses")
print()
#Get info from user
budget = input("Enter Budget:" )

# add expenses
expenses = fuel + hptel + food
remainAmount = budget - expenses

# display results

print("----------Travel Expenses----------")
print("Location:", location)
print("Initial Budget:", budget)
print()
print("Fuel:", fuel)
print("Accomodation:", hotel)
print("Food:", food)
print()
print("Remaining Balance:", remainAmount)
#f"${budget:.2f} to create dollar sign and 2 decimal points after
