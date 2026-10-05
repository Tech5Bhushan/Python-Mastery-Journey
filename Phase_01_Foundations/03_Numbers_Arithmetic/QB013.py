# Q13. Write a Python program to round a floating-point number to a specified number of decimal places.

num = float(input("Enter a floating-point number: "))
places = int(input("Enter the number of decimal places: "))

rounded_num = round(num, places)

print("Rounded number:", rounded_num)