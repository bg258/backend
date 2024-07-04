# --- PYTHON TRY EXCEPT ---
# 1. The "try" block lets you test a block of code for errors.
# 2. The "except" block lets you handle the error.
# 3. "else" block lets you execute code when there is no error.
# 4. The "finally" block lets you execute the code, regardless of the result of the try- and except blocks.

# 1. EXCEPTION HANDLING 
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message. 
# These exceptions can be handled using the try statement: 

try:
    print("Success!")
except:
    print("An exception occurred.")

"""
Since the try block raises an error, the except block will be executed.
Wihout the try block, the program will crash and raise an error.
"""

# 2. MANY EXCEPTIONS
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a 
# special kind of error.
try:
    print("Success!")
except NameError:
    print("Variable x is not defined.")
except:
    print("Something else went wrong!")


# 3. ELSE
# You can use the "else" keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello!")
except:
    print("Something went wrong!")
else:
    print("Nothing went wrong.")

# 4. FINALLY
# The "finally" block, if specified, will be executed regardless if the try block raises an error or not. 
try:
    print("Success!")
except:
    print("Something went wrong!")
finally:
    print("The *try except* is finished.")


# this can be useful to close objects and clean up resources.
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writting to the file!")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file.")


# 5. RAISE AN EXCEPTION
# As a Python developer you can choose to throw an exception if a condition occurs. 
# To throw (or raise) an exception, use the "raise" keyword.
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero.")

# The "raise" keyword is used to raise an exception. 
# you can define what kind of error to raise, and the text to print to the user. 
x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed!")