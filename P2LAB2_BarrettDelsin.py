# Delsin Barrett
# 9/11/2024
# P2LAB2
# Using Dictionaries

#Create a Dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

#Get all keys
keys = cars.keys()

#Print all keys
print(keys)

#Get input from user and assign to variable
user_car = input("Enter a vehicle to see its mpg: ")
print()

#Calculate MPG
print("The", user_car, "gets", cars[user_car], "mpg.")

#Get input (miles traveled) from user
miles = int(input("How many miles will you drive the " + user_car + "? "))
print()

#Calculate gallons needed
gallons_needed = miles/cars[user_car]
print(round(gallons_needed, 2), "gallons of gas are needed to drive the ", user_car, miles, "miles.")

