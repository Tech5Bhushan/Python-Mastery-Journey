# Write a Python program to find the number of notes (Samples of notes 10, 20, 50, 100, 200, 500) against an amount.
# Range - Number of notes(n)  n (1 = n = 1000000).

amount = int(input("Enter the Amount: "))

notes = [500,200,100,50,20,10]

for note in notes:
    count = amount // note

    if count > 0:
        print(f"{note} : {count}")

    amount %= note

# Pythonic Version

amount = int(input("Enter the amount: "))

for note in [500, 200, 100, 50, 20, 10]:
    if amount >= note:
        print(f"{note} : {amount // note}")
        amount %= note


#   // (Floor Division) --> Gives the number of notes.
#   % (Modulus) --> Gives the remainder.