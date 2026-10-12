# Q21. Write a Python program to format a specified string and limit the length of a string.

text = input("Enter the Text: ")
length = int(input("Enter the length of Text: "))
print(text[:length])

# SOLUTION 2 :

text1 = input("Enter the Text: ")
length1 = int(input("Enter the length of Text: "))
print(f"{text1:.{length1}}")


# Using String Formatting

text2 = input("Enter the Text: ")
print("{:.6}".format(text2))