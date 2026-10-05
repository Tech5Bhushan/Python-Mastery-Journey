# Q6. Write a Python program to convert height (in feet and inches) to centimeters.

# FORMULA:
# Total inches = (feet × 12) + inches
# Centimeters = Total inches × 2.54

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

height_cm = (feet * 12 + inches) * 2.54

print("Height in centimeters =", height_cm)


# Alternative Method:

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

height_cm = feet * 30.48 + inches * 2.54

print("Height in centimeters =", height_cm)

# Best Practice

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

cm = (feet * 12 + inches) * 2.54

print(f"Height: {cm:.2f} cm")