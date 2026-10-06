# Q15. Write a Python program to count the number of occurrences of a specific character in a string.

text = "Bhushahhhhhhhhn"

ch = input("Enter a character: ")

if len(ch) == 1:
    print(f"The number of occurrences of '{ch}' is {text.count(ch)}")
else:
    print("Please enter only one character.")


#Alternate Approach:

text = "Bhushahhhhhhhhn"

ch = input("Enter the character: ")

print(f"The number of occurrences of '{ch}' is '{text.count(ch)}'")
