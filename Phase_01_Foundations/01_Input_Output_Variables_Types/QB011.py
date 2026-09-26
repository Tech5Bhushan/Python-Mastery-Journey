# Q11. Write a Python program to add two objects if both objects are integers.

obj1 = 10
obj2 = 20

if isinstance(obj1,int) and isinstance(obj2,int):
    print(obj1+obj2)
else:
    print("Addition is not possible")


# The isinstance() function checks whether an object belongs to a particular data type.