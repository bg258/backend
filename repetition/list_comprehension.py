# Python - List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without a list comprehension you will have to write a "for" statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# THE SYNTAX
# --> newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged. 

# Condition 
# The condition is like a filter that only accepts the items that valuate to True 
newlist = [x for x in fruits if x != "apple"]

# The condition "if x != "apple"" will retur True for all the elements other than "apple", making the new list contain 
# all fruits except "apple".
# The condition is optional and can be omitted. 
newlist = [x for x in fruits]

# ------------------------------------------------------------------------------------------------------------------
# Iterable
# The iterable can be any "iterable" object, like a list, tuple, set etc..
# You can use the range() function to create an iterable
newlist = [x for x in range(10)]

# same example, but with a condition ---> accept only numbers lower than 5. 
newlist = [x for x in range(10) if x < 5]
