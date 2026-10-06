# Q10. Write a Python program to get a newly-generated string from a given string where "Is" has been
# added to the front. Return the string unchanged if the given string already begins with "Is".

sentence = input("Enter the string: ")

if sentence.startswith('Is'):
    print(sentence)
else:
    print('Is '+ sentence)

# More Pythonic Version

sentence = input("Enter the string: ")

print(sentence if sentence.startswith("Is") else "Is " + sentence)