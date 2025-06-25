# helper.py

def greet(name):
    """
    Returns a greeting string for the given name.
    
    Parameters:
    name (str): The name to greet.
    
    Returns:
    str: Greeting message.
    """
    return f"Hello, {name}!"


def add(x, y):
    """
    Returns the sum of two numbers.
    
    Parameters:
    x (float or int): First number.
    y (float or int): Second number.
    
    Returns:
    float or int: Sum of x and y.
    """
    return x + y


def max_of_three(a, b, c):
    """
    Returns the maximum of three numbers.
    
    Parameters:
    a, b, c (int or float): Numbers to compare.
    
    Returns:
    int or float: The largest of the three values.
    """
    return max(a, b, c)


def area_of_rectangle(length, width):
    """
    Calculates the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area calculated as length × width.
    """
    return length * width

if __name__ == "__main__":
    # This code only runs when helper.py is executed directly (not when imported)
    print("This is the helper module containing utility functions.")
    print("Import these functions in main.py to use them!")
    
    # Test calls to verify functions work correctly
    print(greet("Test User"))
    print(add(10, 20))
    print(max_of_three(5, 12, 8))
    print(f"Area of 4x5 rectangle: {area_of_rectangle(4, 5)}")

def greet_default(name="Friend"): #EXTENTION TASK
    """
    Greets with a default name if none is provided.
    """
    return f"Hello, {name}!"

def multiply_all(*args): #EXTENTION TASK
    """
    Multiplies all the numbers provided.
    """
    result = 1
    for num in args:
        result *= num
    return result


def print_profile(**kwargs): #EXTENTION TASK
    """
    Prints key-value pairs from profile information.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def describe_rectangle(length, width): #EXTENTION TASK
    """
    Uses area_of_rectangle and returns a descriptive string.
    """
    area = area_of_rectangle(length, width)
    return f"A rectangle of {length}×{width} has area {area}."


import math
import random
import datetime

def random_circle_area(): #EXTENTION TASK
    """
    Generates a random radius and returns the area of the circle.
    """
    radius = random.uniform(1.0, 10.0)
    area = math.pi * radius ** 2
    return f"Radius: {radius:.2f}, Area: {area:.2f}"

def current_time(): #EXTENTION TASK
    """
    Returns the current date and time.
    """
    return datetime.datetime.now()

