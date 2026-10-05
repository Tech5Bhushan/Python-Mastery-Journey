# Write a Python program that takes a positive integer and calculates the cube root of the number until the number is less than three.
# Count the number of steps to complete the task.
# Sample Data
# (3) - 1
# (39) - 2
# (10000) - 2

num = int(input("Enter the number: "))
count = 0
# new_value = 0
while num>=3:
    num = num**(1/3)
    count += 1

print("The count is:",count)


# Function Version

def cube_root_steps(num):
    count = 0

    while num >= 3:
        num = num ** (1/3)
        count += 1

    return count

print(cube_root_steps(3))      # 1
print(cube_root_steps(39))     # 2
print(cube_root_steps(10000))  # 2
