# PYTHON - ACCESS LIST ITEMS
# List items are indexed and you can access them by reffering to the index number. 
# Example (print the second item of the list)
thislist = ["apple", "banana", "cherry"]
print("Second item of the list: " + str(thislist[1]))
# note: the first item has index 0.

# Negative indexing 
# Negative indexing means start from the end. 
# -1 refers to the last item, -2 refers to the second last item etc...
thislist = ["apple", "banana", "cherry"]
print("The last item of the list: " + str(thislist[-1]))

# Range of indexes
# You can specify a range of indexes by specifying where to start and where to end the range. 
# When specifying a range, the return value will be a new list with the specified items. 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Range of indexes: " + str(thislist[2:5]))
