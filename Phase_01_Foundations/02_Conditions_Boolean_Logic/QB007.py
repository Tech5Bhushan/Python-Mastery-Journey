# Q7. Write a Python program to perform an action if a condition is true. Given a variable name, if the
# value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.

var_name = int(input("Enter the value: "))
if var_name == 1:
    print("First day of a Month!")
else:
    pass

# Alternative One-Liner

var_name = int(input("Enter the value: "))
print("First day of a Month!") if var_name == 1 else None