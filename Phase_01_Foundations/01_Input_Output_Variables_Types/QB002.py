# Q2. Write a Python program to find out what version of Python you are using.


# Solution 1: Using sys.version
import sys

print("Python Version: ", sys.version)

# Solution 2: Using platform.python_version()

import platform
print(platform.python_version())