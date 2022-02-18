# Inheritence
import turtle 

# Creating a Canvas instance.
# Object instance of Turtle class.
myturtle = turtle.Turtle()

myturtle.penup()
myturtle.goto(50, 75) # Place the turle on certain cordinate.
# Throws an straight line.

myturtle.pendown()
myturtle.forward(100)
myturtle.left(90) # In degrees.
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()