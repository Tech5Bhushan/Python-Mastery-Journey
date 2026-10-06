# Q14. Write a Python program to concatenate N strings.

# SOLUTION 1 : USING WHILE LOOP

n = 0
result = ""
while n != 3:
    var = input("Enter the strings: ")
    result += var
    n +=1
print("The concatenated string is: ", result)

#SOLUTION 2 : USING FOR LOOP

n = int(input("How many strings? "))

result = ""

for i in range(n):
    s = input("Enter a string: ")
    result += s

print("Concatenated String:", result)


#SOLUTION 3: USING a List and join() (Recommended)

n = int(input("How many strings? "))
strings = []
for i in range(n):
    strings.append(input("Enter the string:"))

result = "".join(strings)

print(result)

# If You Want Spaces Between Strings

n = int(input("How many strings? "))

strings = []

for i in range(n):
    strings.append(input("Enter a string: "))

print(" ".join(strings))

