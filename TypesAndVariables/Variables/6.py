
import math

your_height=float(input("What is your height in meters? "))
h=float(input("Type your height above the see level in meters: "))
elevation=your_height+h

h_sqrt= math.sqrt(elevation)
d=h_sqrt*3.57

print("You are ", d ,"km from the horizon")