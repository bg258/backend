# Python  - Add List Items
# Append Items
# To add an item to the end of the list, use the "append()" method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items 
# To insert a list item at a specified index, use the insert() method. 
# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# --------------------------------------------------------------------------------
# Extended list
# To append elements from "another list" to the current list, use the "extended()" method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # The elements will be added to the end of the list. 

# Add Any Iterable
# The "extend()" method does not have to append "lists", you can add any iterable object (tuples, set, dictionaries)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)




