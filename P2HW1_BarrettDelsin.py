# Delsin Barrett
# 9/11/2024
# P1HW2
#create program on IDLE

print("This program calculates and displays travel expenses")
print()
#Get info from user
budget = int (input("Enter Budget: " ))
print()
location = input("Enter your travel destination: ")
print()
fuel = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you  need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
# add expenses
expenses = fuel + hotel + food
remainAmount = budget - expenses

# display results

print("----------Travel Expenses----------")
print("Location:", location)
print("Initial Budget:", f"${budget:.2f}")
print()
print("Fuel:", f"${fuel:.2f}")
print("Accomodation:", f"${hotel:.2f}")
print("Food:", f"${food:.2f}")
print()
print("Remaining Balance:", remainAmount)
#f"${budget:.2f}" to create dollar sign and 2 decimal points after
