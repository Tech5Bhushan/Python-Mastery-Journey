# Q18. A Python list contains two positive integers. Write a Python program to check whether the cube root of the first number is equal to the square root of the second number.
# Sample Data
# ([8, 4]) - True
# ([64, 16]) - True
# ([64, 36]) - False

lst = [8,4]
cube_root = lst[0]**1/3
sqr_root = lst[1]**0.5

print(round(cube_root,10) == round(sqr_root,10))

# Better Function Version

def check_roots(nums):
    return round(nums[0] ** (1/3), 10) == round(nums[1] ** 0.5, 10)

print(check_roots([8, 4]))     # True
print(check_roots([64, 16]))   # True
print(check_roots([64, 36]))   # False

# Another Simple Approach

nums = [64, 16]

if round(nums[0] ** (1/3), 10) == round(nums[1] ** 0.5, 10):
    print(True)
else:
    print(False)