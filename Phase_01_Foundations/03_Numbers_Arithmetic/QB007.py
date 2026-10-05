# 7. Write a Python program to convert the distance (in feet) to inches, yards, and miles.

# Formula
#
# 1 foot  = 12 inches
# 1 yard  = 3 feet
# 1 mile  = 5280 feet

feet = float(input("Enter distance in feet: "))

inches = feet * 12
yards = feet / 3
miles = feet / 5280

print("Distance in inches:", inches)
print("Distance in yards:", yards)
print("Distance in miles:", miles)


# Better Formatted Version

feet = float(input("Enter distance in feet: "))

inches = feet * 12
yards = feet / 3
miles = feet / 5280

print(f"Inches: {inches:.2f}")
print(f"Yards : {yards:.2f}")
print(f"Miles : {miles:.4f}")
