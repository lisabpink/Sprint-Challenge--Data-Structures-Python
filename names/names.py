# Original Runtime: 8.093192100524902 seconds

from binary_search_tree import BSTNode
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Binary Search Tree runtime: 0.15172886848449707 seconds------------------
bst = BSTNode("")
for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)
# END Binary Search Tree runtime: 0.15172886848449707 seconds------------

# STRETCH GOAL YAASSS
# Python's efficient key/value hash table structure is called a "dict".
# The "empty dict" is just an empty pair of curly braces {}. Looking up or
# setting a value in a dict uses square brackets, e.g. dict['foo'] looks
# up the value under the key 'foo'. Strings, numbers, and tuples work as
# keys, and any type can be a value. -Google

# runtime: 0.004703998565673828 seconds------------------------------------
names = {}

for value in names_1:
    names[value] = True

for value in names_2:
    if value in names:
        duplicates.append(value)
# END runtime: 0.004703998565673828 seconds seconds-------------------------------------

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# set()
# list()

# loop back to this after MVP
