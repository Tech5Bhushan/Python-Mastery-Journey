# Q5. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

# The distance between two points is calculated using the Distance Formula: ((x2 - x1) ** 2 + (y2 - y1) ** 2)

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Distance =", distance)

# Simpler Solution Using math.dist()

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

print(math.dist((x1, y1), (x2, y2)))

# Best Practice

import math

x1, y1 = map(float, input("Enter x1 y1: ").split())
x2, y2 = map(float, input("Enter x2 y2: ").split())

distance = math.dist((x1, y1), (x2, y2))

print(f"Distance = {distance:.2f}")