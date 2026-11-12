import subprocess
subprocess.run("cls", shell=True)

# A module is a Python file (.py) that contains code you can reuse: functions, variables, and classes. You bring that code into your program with 'import'.

# There are 3 types of modules
# 1. Built-in modules(standard library)
# 2. External modules
# 3. User-defined modules

# Package -> modules -> functions

# =====================
# 1. Built-in Module 
# =====================
# built-in modules such as math, random, datetime

import math

# print(math.sqrt(16))    
# print(math.pi) 

# =====================
# 2. dir()
# =====================
# dir() returns a list of names (functions, variables, methods) that an module contains.

# for name in dir(math):
#     print(name)

# ========================
# 3. help() and __doc__
# ========================

# help(math.sqrt)        # explanation of one function
# print(math.sqrt.__doc__)
# help(math)             # full manual (press q to quit)

# =============================
# 4. Way to import
# =============================
# 4.1. Import the whole module (brings in the module as one named object and reach functions through the module’s name)
# import math
# print(math.sqrt(25))

# 4.2 Import with a short nickname (alias)
# import math as m
# print(m.sqrt(25))

# 4.3 Import only what you need
# from math import sqrt, pi
# print(sqrt(25), pi)          # no 'math.' needed

# 4.4 Import with a nickname for one item
# from math import factorial as fact
# print(fact(5))               # 120

# 4.5 Import everything (avoid this ⚠️)
# from math import *
# print(sqrt(16))       
# print(pi)

# ℹ️ from module import * copies all of the module’s public names straight into your file, so you use them without the prefix.
# ⚠️ import * could lead to overwrite your own variables and cannot tell where a name came from.

# =============================
# 5. External modules 
# =============================
# External (third-party) modules are written by other developers and shared on PyPI (the Python Package Index).

# Some useful pip commands:


# pip list                    # show installed packages
# pip show requests           # details about one package
# pip install requests
# pip install --upgrade requests
# pip uninstall requests

# import requests
# response = requests.get('https://dummyjson.com/carts')
# print(response.json())

# =============================
# 6. User-defined modules 
# =============================
import circle

result = circle.area(2)
print(result)
