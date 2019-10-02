import math

mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (meters/sec.): "))

momentum = mass * velocity
kineticEnergy = (1/2) * mass * math.pow(velocity, 2)

print("The object's momentum is", momentum)
print("The object's kinetic energy is", kineticEnergy)
