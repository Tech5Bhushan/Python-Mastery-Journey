# Q72. Write a Python program to display a number in left, right, and center aligned with a width of 10.

num = input("Enter the number: ")

print(f"Left Align: '{num:<10}'")
print(f"Right Align: '{num:>10}'")
print(f"Center Align: '{num:^10}'")