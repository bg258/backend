# Python - Loop Lists 
# You can loop through the list items by using a "for" loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by reffering to their index number. 
# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using a WHILE loop
# You can loop through the list items by using a "while" loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items 
# by reffering to their indexes. Remember to increse the index 1 after each iteration.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping using List Comprehension
# List comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
