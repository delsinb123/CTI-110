# Delsin Barrett
# 9/11/2024
# P2LAB1
# Calculate math related to a circle

#Import the math library
import math

#Get float imput from user (radius)
radius = float(input("What is the radius of the circle? "))
print()

#Calculate Diameter
diameter = radius * 2
print("The diameter of the circle is", diameter)
print()

#Calculate Circumfrence
circumfrence = 2 * math.pi * radius
print("The circumfrence of the circle is", round(circumfrence, 2))
print()

#Calculate Area
area = math.pi * (radius ** 2)
print("The area of the circle is", round(area, 3))
