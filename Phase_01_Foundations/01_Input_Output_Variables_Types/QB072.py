# Q72. Write a Python program to display a number in left, right, and center aligned with a width of 10.

num = input("Enter the number: ")

print(f"Left Align: '{num:<10}'")
print(f"Right Align: '{num:>10}'")
print(f"Center Align: '{num:^10}'")

# Alternative Using format()

num1 = input("Enter the number: ")

print(format(num1, "<10"))
print(format(num1, ">10"))
print(format(num1, "^10"))

# <10 --> Left align within width 10
# >10 --> Right align within width 10
# ^10 --> Center align within width 10