# Q25. Write a Python program to clear the screen or terminal.

import os

os.system('cls' if os.name == 'nt' else 'clear')

# To clear the terminal screen, use the os.system() function.
# Windows uses the command: cls
# Linux/macOS uses the command: clear
# The code automatically detects the operating system: os.name == 'nt'
# nt → Windows
# otherwise → Linux/macOS

# Windows Only Version

import os

os.system("cls")