import math

radius = float(input("Enter the radius of the sphere: "))
print("Radius = ", radius)
# Diameter
diameter = radius * 2

# Circumference
circumference = diameter * math.pi

# Surface Area
surfaceArea = 4 * math.pi * radius * radius

# Volume
volume = (4/3) * math.pi * radius * radius * radius

print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface area: ", surfaceArea)
print("Volume: ", volume)
