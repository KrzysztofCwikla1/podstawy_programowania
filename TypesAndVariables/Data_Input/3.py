###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

volume = a * b * c
print(f"volume = {volume}")

surface_area = 2 * (a*b + a*c + b*c)
print(f"surface area = {surface_area}")