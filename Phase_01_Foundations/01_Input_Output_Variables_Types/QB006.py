# 13. Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# Solution 1 :

print("""a string that you "dont\'t" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

# Solution 2 :

print("a string that you \"don\'t\" have to escape \nThis \nis a ....... multi line\nheredoc string ---------> example")