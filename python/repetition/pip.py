# ----------- PYTHON PIP -----------
"""
What is PIP?
PIP is a package manager for Python packages, or modules if you like."""

# WHAT IS A PACKAGE?
# A package contains all the files you need for a module. 
# Modules are Python code libraries you can include in your project. 

# DOWLOAD A PACKAGE
# Downloading a package is very easy. Open the command line interface and tell PIP to dowload 
# the package you want. Navigate your command line to the location of Pythons script directory, 
# and type the following: 

"""pip install camelcase"""

import camelcase
c = camelcase.CamelCase()
txt = "Hello World!"
print(c.hump(txt))

# REMOVE A PACKAGE
# Use the "uninstall" command to remove a package:
"""pip uninstall camelcase"""

# LIST PACKAGES
# Use the "list" command to list all the packages installed on your system.
"""pip list"""