import subprocess
subprocess.run("cls", shell=True)

# A function is a named block of code that does one job. 
# Example of built-in functions in Python: print(), len(), type(), max(), sum()

# print(len('hello'))
# print(max(3, 9, 2))

# ========================
# 1. Syntax 
# ========================

# def function_name(parameters):
#     statements
#     return value      # optional

# Example

# def greet(name):
#     return print(f"Hello, {name}!")

# greet("Sara") # calling a function

# ===================================
# 2. Parameters and arguments
# ===================================
# Parameter: the variable name in the function definition.
# Argument: the actual value you pass when calling.

# def greet(name):          # name is a PARAMETER
#     print('Hello,', name)

# greet('Sara')             # 'Sara' & 'ali' is an ARGUMENT
# greet('Ali')

# Note: order matters when there are several parameters

def introduce(name, age):
    print(name, 'is', age, 'years old')

# introduce('Sara', 20)
# introduce(20, 'Sara')  # wrong order

# for easier to read and avoid wrong order we can pass argument by name
# introduce(name='Sara', age=20)

# ===================================
# 3. Default Parameters
# ===================================

# def greet(name, greeting='Hello'):
#     print(greeting + ', ' + name)

# greet('Sara')             
# greet('Sara', 'Good Morning!')  

# ===================================
# 3. *args
# ===================================
# The * collects extra positional arguments into a tuple.

def total(*args):
    print(args)           # (1, 2, 3) -> tuple
    return sum(args)

# print(total(1, 2, 3))
# print(total())

# ===================================
# 4. **kwargs
# ===================================
# The ** collects extra keyword arguments into a dictionary.

def show_profile(**kwargs):
    print(type(kwargs))         # type = dict
    for key, value in kwargs.items():
        print(key, '=', value)

# show_profile(name='Sara', age=20)

# [using both *args and **kwargs]

# def demo(a, b=10, *args, **kwargs):
#     print(a, b, args, kwargs)

# demo(1, 2, 3, 4, x=5, y=6)    

# ========================
# 5. return statement 
# ========================
# Note: function stop when it met return statement.

# def check(n):
#     if n > 0:
#         return "positive"
#     return "not positive"   # only reached if the first return didn't run

# Use return statement when you want to:
# - Gives a value back
# - Store in a variable
# - use in other calculations

# ===================================
# Example: with return statement
# ===================================

def add(a, b):
    return a + b

# result = add(2, 3)
# print(result)        
# print(add(2, 3) * 10)  

# ===================================
# Example: without return statement
# ===================================

# def add(a, b):
#     print(a + b)

# result = add(2, 3)  
# print(result)        # None
# print(add(2, 3) * 10)  # TypeError (None * 10)

# [Returning multiple values]
# Note: Python returns multiple values as a tuple

def min_max(numbers):
    return min(numbers), max(numbers)

# result = min_max([4, 8, 1, 9])
# print(type(result))

# low, high = result
# print(f"Smallest Number: {low}, Largest Number: {high}")

# ===================================
# 6. pass
# ===================================
# pass does nothing. 
# Python needs at least one statement in a function body, so use pass as a placeholder when you plan to write the code later.

def calculate_tax():
    pass

# calculate_tax()  

# ===============================================
# 7. Good Practice: Docstrings and type hints
# ===============================================
# A docstring explains what the function does. 
# Type hints show the expected types (they are hints only and are not enforced).

def area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height

# help(area)                    # shows the docstring

# ===============================================
# 8. Recursion
# ===============================================
# Recursion means a function calls itself. Every recursive function needs:
# 1. Base case: when to stop.
# 2. Recursive case: a call to itself with a smaller input or a reduced task, making progress toward the stopping condition (base case)

def factorial(n):
    if n == 0 or n == 1:      # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(4))

# [How recursive runs]:

# factorial(4)
# = 4 * factorial(3)
# = 4 * (3 * factorial(2))
# = 4 * (3 * (2 * factorial(1)))
# = 4 * (3 * (2 * 1))
# = 4 * (3 * 2)
# = 4 * 6
# = 24

# [Recursion vs Loop]
# Same: repeat task
# Difference: 
# 1. A loop repeats a block of code until a condition stops it.
# 2. Recursion is a function that calls itself with a smaller version of the problem until it reaches a stopping point.

# ===============================================
# 9. Lambda
# ===============================================
# A lambda is a small, one-line, anonymous function.

# [Syntax]
# lambda parameters: expression

# square = lambda x: x * x
# print(square(5))

# add = lambda a, b: a + b
# print(add(2, 3))

# ===================================
# 10. Functions are values
# ===================================
# Functions can be stored in variables and passed to other functions.

def convert_upper(text):
    return text.upper()

def convert_lower(text):
    return text.lower()

def apply(func, value):
    return func(value)

print(apply(convert_upper, 'hello'))  
# # print(apply(convert_lower, 'hello'))  

