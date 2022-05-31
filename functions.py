# ********Day 54 Start**********
# Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# ##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
# def calculate(calc_function,n1,n2):
#     return calc_function(n1,n2)
#
# result = calculate(add,2,3)
# print(result)
#
# #Nested Functions
# def outer_function():
#     print("I am outer")
#
#     def nested_function():
#         print("I am inner")
#
#     nested_function()
#
# outer_function()
#
# #Functions can be returned from other functions
# def outer_function():
#     print("I am outer")
#
#     def nested_function():
#         print("I am inner")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function()


#Python Decorator Function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

def say_greeting():
    print("How are you? ")

say_hello()