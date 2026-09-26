# Q29. Write a Python program to empty a variable without destroying it.


# SOLUTION 1

a = 'Bhushan'
a = ''
print(a)

# SOLUTION 2

b = 'Bhushan'
b = None
print(b)

# For Lists
nums = [1,2,3,4,5]
nums.clear()
print(nums)