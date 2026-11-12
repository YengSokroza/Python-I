import subprocess
subprocess.run("cls", shell=True)

# ======================================
# 1. Exception handling Keywords 
# =======================================

# There are two sides of exception handling
# 1. Raising an exception: trigger an exception manually / Useful for enforcing validation rules and business logic.
# 2. Catching an exception: deciding what to do when something goes wrong (try / except, else, finally)

# ================================
#  try / except
# ================================

def divide_numbers(a, b):
    try:
        result = a / b
        return result

    except ZeroDivisionError:
        return "Cannot divide by zero."


# print(divide_numbers(10, 2))
# print(divide_numbers(10, 0))

# ========================================
# try / except / else / finally
# ========================================

def calculate_average(total, count):
    try:
        average = total / count

    except ZeroDivisionError:
        print("Error: Count cannot be zero.")

    # ℹ️ if you don't know exactly what exception might happen, you can use a general exception handler

    # except Exception as error:
    #     print("Something went wrong:", error)

    else:
        # Runs only when no exception occurs
        print("Average:", average)

    finally:
        # Always runs, whether an exception occurs or not
        print("Calculation finished.")


# calculate_average(100, 5)
# calculate_average(100, 0)

# ========================================
# 2. Exception types 
# ========================================
# Common built-in exception types: TypeError, ValueError, ZeroDivisionError, FileNotFoundError, KeyError, IndexError

# TypeError
# Happens when we use an inappropriate data type.

def add_numbers(a, b):
    return a + b


# try:
#     print(add_numbers(10, "20"))

# except TypeError:
#     print("Error: Both values must be numbers.")


# ========================================
# ValueError
# ========================================
# Happens when the data type is correct, but the value is not appropriate.

def convert_age(age):
    return int(age)


# try:
#     print(convert_age("twenty"))

# except ValueError:
#     print("Error: Age must be a number.")


# ========================================
# ZeroDivisionError
# ========================================

# try:
#     result = 10 / 0

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")


# ========================================
# FileNotFoundError
# ========================================

# try:
#     file = open("student.txt", "r")

# except FileNotFoundError:
#     print("Error: File does not exist.")


# ========================================
# KeyError
# ========================================

student = {
    "name": "Dara",
    "age": 20
}

# try:
#     print(student["email"])

# except KeyError:
#     print("Error: The key does not exist.")


# ========================================
# IndexError
# ========================================

numbers = [10, 20, 30]

# try:
#     print(numbers[5])

# except IndexError:
#     print("Error: Index is outside the list.")

# ========================================
# 3. Validation techniques 
# ========================================
# Validation means checking whether data is acceptable before using it.
# isinstance() checks: manual validation
# decorators such as @enforce_types: automated validation
# pydantic, typeguard: validation libraries

# ========================================
# isinstance()
# ========================================

# isinstance() checks whether a value belongs to a particular data type.

def register_student(name, age):

    # Validate the name
    if not isinstance(name, str):
        return "Name must be a string."

    # Validate the age
    if not isinstance(age, int):
        return "Age must be an integer."

    # Validate the age range
    if age < 18:
        return "Student must be at least 18 years old."

    return "Student registered successfully."


# print(register_student("Dara", 20))
# print(register_student("Dara", "20"))
# print(register_student("Dara", 15))

# In larger projects, developers can use libraries or decorators to automatically validate function inputs.

def enforce_types(func):

    #The validation checkpoint
    def wrapper(number):

        if not isinstance(number, (int, float)):
            raise TypeError("Number must be an integer or float.")

        return func(number)

    return wrapper


@enforce_types
def calculate_cube(number):
    return number ** 3

# print(calculate_cube(3))

# try:
#     print(calculate_cube("3"))

# except TypeError as error:
#     print("Error:", error)


# ============================================================
# 5. CUSTOM EXCEPTION
# ============================================================

# Python provides many built-in exceptions.
# But sometimes our program needs a specific error​​​​​​​​for a specific situation.
# We can create our own exception by inheriting from Ex​​​ception.


# class InvalidAgeError(Exception):

#     def __init__(self, age):​​​​​​​​​​​​​​​​​
# ​​​​​
#         self.age = age

#         super().__init__(
#             f"Invalid age: {age}. Age must be between 18 and 100."
# )

# def check_age(age):

#     if age < 18 or age > 100:
#         raise InvalidAgeError(age)

#     return "Age is valid."


# try:
#     print(check_age(25))
#     print(check_age(15))

# except InvalidAgeError as error:
#     print("Error:", error)

