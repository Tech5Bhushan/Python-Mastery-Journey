# Q3. Write a Python program to get the volume of a sphere with radius six.
# V = ((4/3)*pi*r**3)

import math

r = 6
sphere_volume = (4/3) * math.pi * (r**3)
print("The volume of the sphere is: ",sphere_volume)


# BEST PRACTICE

import math

radius = 6
volume = (4 / 3) * math.pi * radius ** 3

print(f"Volume of sphere: {volume:.2f}")
