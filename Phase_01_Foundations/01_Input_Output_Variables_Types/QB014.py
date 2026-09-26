# Q14. Write a Python program that calls an external command.

import os
os.system("echo Hello World")


# Alternate solution

import subprocess

subprocess.run("echo Hello World", shell=True)