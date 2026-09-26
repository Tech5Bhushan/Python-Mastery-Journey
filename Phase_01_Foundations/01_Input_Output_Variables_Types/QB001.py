# Q1. Write a Python program to get the index of the first element which is greater than a specified
# element.

lst = [1,2,3,4,5,6,7]
element = int(input("Enter the element: "))
for i in range(len(lst)):
    if lst[i]>element:
        print("The index of first element which is greater than specified", element, 'is :',i, "and first greater element is", lst[i] )
        break

