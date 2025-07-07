"""
Utility functions module.
"""

def add(a, b):
    """
    Add two numbers together.

    Parameters:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: Sum of a and b.
    """
    return a + b


def is_even(n):
    """
    Check if a number is even.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if n is even, False otherwise.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n % 2 == 0


def get_largest(numbers):
    """
    Find the largest number in a list.

    Parameters:
        numbers (list): A list of numeric values.

    Returns:
        int | float: The largest number in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
    return max(numbers)


def reverse_string(s):
    """
    Reverse a string.

    Parameters:
        s (str): Input string.

    Returns:
        str: The reversed string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]
