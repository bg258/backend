# ----------- 1. F STRINGS -----------
txt = f"The price is 49 dollars."
print(txt)

# Placeholders and Modifiers
# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions
# and modifiers to format the value. 
price = 59
txt = f"The price is {price} dollars"
print(txt)

# a placeholder can also include a "modifier" to format the value
# a modifier is included by adding a colon : followed by a legal formatting type, like 2.f 
# which means fixed point number with 2 decimals. 

price = 11
txt = f"The price is {price:.2f} dollars"
print(txt)

# you can also format a value directly without keeping it in a variable. 
txt = f"The price is {95:.2f} dollars"
print(txt)

# 2. Perform operations in F-strings
# You can perform Python operations inside the placeholders. 
# You can do math-operations: 

txt = f"The price is {20 * 59} dollars"
print(txt)

# You can perform math operations on variables: 
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# You can perform "if...else" statements inside the placeholders.
price = 49
txt = f"It is very {"Expensive" if price > 50 else "Cheap"}"
print(txt)

# 3. Execute Functions in F-Strings
# You can execute functions inside the placeholder.

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

# The function doest not have to be a built-in python method, you can create your own functions and use them:
def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# 4. More modifiers
# At the beginning of this chapter we explained how to use the .2f modifier to format a number into a fixed point number 
# with 2 decimals. There are several other modifiers that can be used to format values: 
price = 590000
txt = f"The price is {price:,} dollars"
print(txt)

# 5. String format()
# Before Python 3.6 we used the format() method to format strings. 
# The format() method can still be used, but f-strings are faster and the preferred way to format strings. 
# The next examples in this page demonstrates how to format strings with the format() method. 
# The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))


# You can add parameters inside the curly brackets to specify how to convert the value: 
price = 11
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# An add more placeholders:
quantity = 3
itemno = 567 
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# 6. Index numbers 
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed
# in the correct placeholders: 
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Also if you want to refer to the same value more than once, use the index number: 
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# 7. Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use 
# names when you pass the parameter values txt.format(carname = "Ford")
myorder = "I have a {carname}, it is a {model}"
print(myorder.format(carname = "Ford"), model = "Mustang")



