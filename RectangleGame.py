# Rectangle game.
from cmath import sqrt
from random import randint

class Point: # Name of the class. Use CamelCase
    
    # Minimum requires.
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Method.
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
            and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    # Distance method.
    def distance_from_point(self, xp, yp):
        dist = (self.x  - xp)**2 + (self.y - yp)**2
        dist **= 0.5
        print(dist)

# Rectangle Class.
class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
    
    def calculate_area(self):
        self.area = (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)
        return str(self.area)
    

rectangle = Rectangle(
    Point(randint(0,9), randint(0,9)), Point(randint(10,19), randint(10,19))
)

print(rectangle.calculate_area())

print("Rectangle coordinates: ", 
      rectangle.lowleft.x, ",",
      rectangle.lowleft.y, "and",
      rectangle.upright.x, ",",
      rectangle.upright.y)

user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

user_area = float(input("Guess rectangle are: ")) 

print("Your point was inside the rectangle: ", user_point.falls_in_rectangle(rectangle))
print("You have failed by: ", rectangle.area - user_area)

# What's self?
# Self is the variable that holds the object instance that is being created by that class.

# init method vs normal method
# init is used when you declare de object meanwhile normal 
# it's only used when you call it.