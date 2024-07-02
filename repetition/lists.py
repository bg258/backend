# PYTHON LISTS
mylist = ["apple", "banana", "cherry"]

# List
# Lists are used to store multiple items in a single variable
print("1. Python lists\n", mylist)

# List items
# List items are orrdered, changeable, and allow duplicate values. List items 
# are indexed, the first item has index [0], the second item has index [1] etc..

# Ordered 
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change. 
# If you add new items to a list, the new items will be placed at the end of the list. 

# Changeable 
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created. 

# Allow duplicates 
# Since lists are indexed, lists can have items with the same value
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("2. Allow duplicates \n", thislist)

# ---------------------------------------------------------------------------------------------------
# List lenght
# To determine how many items a list has, use the "len" function:
thislist = ["apple", "banana", "cherry"]
print("3. List length " + str(len(thislist)))

# List items - Data types
# List items can be of any data type (string, int and boolean data types)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 3, 5, 7, 9]
list3 = [True, False, False]

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
# ---------------------------------------------------------------------------------------------------
# Type()
# From Python perspective, lists are defined as objects with the data type "list":
# <class "list">
mylist = ["apple", "banana", "cherry"]
print("4. Type() \n", type(mylist))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list. 
thislist = list(("apple", "banana", "cherry")) # note the double round brackets
print("5. List() constructor \n", thislist)


