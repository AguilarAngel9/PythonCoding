# Inheritence
import turtle 

# Creating a Canvas instance.

myturtle = turtle.Turtle() # Object instance of Turtle class.

myturtle.penup() # Do not touch the canvas.
myturtle.goto(50, 75) # Place the turle on certain cordinate. Throws an straight line.

myturtle.pendown() # Touch the canvas.
myturtle.forward(100)
myturtle.left(90) # In degrees.
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done() # Keep the Graphics interface