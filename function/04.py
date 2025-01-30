#Problem: Create a function that returns both the area and circufrence of a circle given its radius.


import math

def circle_status(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_status(3)

print("Area: ",a, "Circumference: ", c)
