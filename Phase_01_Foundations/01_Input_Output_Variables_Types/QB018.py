# Q18. Write a Python program to get the height and width of the console window.

import os
from shutil import get_terminal_size

size = os.get_terminal_size()
print(size)
# print("Height: ", size.columns)
# print("Width: ", size.lines)

# For Pycharm

from shutil import get_terminal_size

size = get_terminal_size(fallback=(80, 24))

print("Width :", size.columns)
print("Height:", size.lines)