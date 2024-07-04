# Python - Sort Lists
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print("Before sorting: " + str(thislist))
thislist.sort()
print("After sorting: " + str(thislist))

# Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# -------------------------------------------------------------------------------------------
# Sort descending 
# Sort the list descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print("Reversing list: " + str(thislist))

# Sort the list descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function
# The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

#-----------------------------------------------------------------------------------------------
# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted 
# before lower case letters.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list. 
# So if you want a case-sensitive sort function, use str.lower as a key function
thislist = ["banana", "Orange", "Kiwi", "CHERRY"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse order 
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverrses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "Cherry"]
thislist.reverse()
print(thislist)


