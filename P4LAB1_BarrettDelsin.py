#Delsin Barrett
#9/23/2024
#P4LAB1
#Use turtle to draw shapes with loops


#import the turtle library for drawing
import turtle

#create a window for a turtle to draw in
window = turtle.Screen()

#create a turle object
tom = turtle.Turtle()

#Forward loop to draw a square
for side in range(4):
    tom.forward(50)
    tom.right(90)

#While loop to draw triangle
tri = 0
while tri < 3:
    tom.forward(50)
    tom.left(120)
    tri = tri + 1
