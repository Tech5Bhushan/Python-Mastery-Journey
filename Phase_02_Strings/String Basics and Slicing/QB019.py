# Q19. Write a Python program to print Unicode characters

# Unicode characters can be printed using the built-in chr() function, which converts a Unicode code point (integer) into its corresponding character.

for i in range(65, 91):
    print(chr(i), end=" ")

# Print Unicode Characters with Their Values

for i in range(65, 71):
    print(i, "->", chr(i))

# Print Some Special Unicode Characters

print("\u00B2")  # ²
print("\u00B3")  # ³
print("\u03C0")  # π
print("\u20B9")  # ₹