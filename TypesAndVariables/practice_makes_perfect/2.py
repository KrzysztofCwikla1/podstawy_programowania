import math

PI = 3.14

radius = float(input("r = "))

area = PI * math.pow(radius,2)
circumference = 2 * PI * radius 

print(f"circumference = {circumference:.2f}, area = {area:.2f}")
