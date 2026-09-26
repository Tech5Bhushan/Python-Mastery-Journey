# Q17. Write a Python program to print to STDERR

# SOLUTION :
# In Python, STDERR (Standard Error) is used to display error messages and diagnostic information.

import sys
print("This is an error message",file=sys.stderr)

# Alternative Solution Using sys.stderr.write()

import sys
sys.stderr.write("This is an error message\n") # Note: sys.stderr.write() does not automatically add a newline, so \n is needed.

#EXPLANATION:

# Python provides three standard streams:
#
# stdin   -> Input
# stdout  -> Normal output
# stderr  -> Error output
#
# Example:
#
# import sys
#
# print("Normal Message")
# print("Error Message", file=sys.stderr)
#
# Output:
#
# Normal Message      # stdout
# Error Message       # stderr