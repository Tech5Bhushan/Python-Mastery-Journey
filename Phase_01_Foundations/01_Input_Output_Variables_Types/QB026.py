# Q26. Write a Python program to get system command output

import subprocess

result = subprocess.run(["ipconfig"],capture_output=True,text=True)

print(result.stdout)