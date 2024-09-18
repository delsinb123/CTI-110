# Delsin Barrett
# 9/4/2024
# P3HW2
# Calculate coins needed for change


#Floor Division // Gives you whole number from division

#Modulus % Gives you back the remainder from division

#Get Amount of moeny
amount = float(input("Enter the amount of money as a float: "))

#Convert value into integer. Last 2 digits are still change
int_amount = int(round(amount * 100))
print(int_amount)
