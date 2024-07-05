# Python - Join Lists
# There are several ways to join, or concatenate, two or more lists in Python 
# One of the easist ways are by using the + operator 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["L.Yamal", "A.Morata", "N.Williams"]
list2 = ["Rodri", "A.Laporte", "M.Cucurella"]

for fotballer in list2:
    list1.append(fotballer)

print("Spanish squad 2024 (Euro): " + str(list1))

# or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1 = ["L.Yamal", "A.Morata", "N.Williams"]
list2 = ["Rodri", "A.Laporte", "M.Cucurella"]
list1.extend(list2)
print(list1)