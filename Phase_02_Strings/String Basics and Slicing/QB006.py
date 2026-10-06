# Q6. Write a Python program to remove duplicate words from a given list of strings.

words = ["apple", "banana", "orange", "grapes","grapes","banana"]
e_lst = []
for word in words:
    if word not in e_lst:
        e_lst.append(word)
print(e_lst)

# Above code
# ✅ Removes duplicates
# ✅ Preserves the original order of elements


#Using set:

words = ["apple", "banana", "orange", "grapes","grapes","banana"]
print(set(words))

# Above code
# ✅ Very short
# ✅ Automatically removes duplicates
# ❌ Does not preserve the original order


# Best Pythonic Solution (Preserves Order)

words = ["apple", "banana", "orange", "grapes", "grapes", "banana"]

result = list(dict.fromkeys(words))

print(result)

# How it Works
# dict.fromkeys(words) creates
#
# {
#     'apple': None,
#     'banana': None,
#     'orange': None,
#     'grapes': None
# }
#
# Since dictionary keys must be unique, duplicates are automatically removed.