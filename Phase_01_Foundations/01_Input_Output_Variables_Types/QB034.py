# Q34. Write a Python program to print a variable without spaces between values. Sample value : x =30


x = 30
print("The value of x =",x) #--> This adds a default space between = and x (value)

#Solution 1: using f-string

x = 30
print(f"The value of x={x}")

#Solution 2: using sep=

x= 30
print("The value of x=",30,sep='')

