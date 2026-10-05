# Q9. Write a Python program to check whether a given employee code is exactly 8 digits or 12 digits.
# Return True if the employee code is valid and False if it's not.

emp_code = input("Enter the Employee Code: ")
print(True if len(emp_code) == 8 or len(emp_code) == 12 else False)
