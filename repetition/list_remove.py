# Python  - Remove List Items
# The remove() method the specified item.
thislist = ["apple", "banana", "cherry"]
print("Before remove: " + str(thislist))
thislist.remove("banana")
print("After remove: " + str(thislist))

# If there are more than one item with the specified value, the remove() method removes the first occurence. 
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# -------------------------------------------------------------------------------------
# Remove Specified Index
# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item. 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# the "del" keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# the "del" keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the list 
# The clear() method empties the list. 
# The list still remains, but it has no content. 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

