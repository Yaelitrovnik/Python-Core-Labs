# main.py

from helper import greet, add, max_of_three, area_of_rectangle, current_time, random_circle_area, describe_rectangle, print_profile, multiply_all, greet_default

print("---CORE TASKS---")

# Call greet()
print(f"Greet message: {greet("Yael")}")

# Call add()
print(f"Sum result: {add(10, 5)}")

# Call max_of_three()
print(f"Maximum value: {max_of_three(3, 7, 5)}")

# Call custom area_of_rectangle()
print(f"Area of rectangle: {area_of_rectangle(4, 6)}")

print("---EXTENTION TASKS---")

# 1. Default parameter
print(f"Greet with default: {greet_default()}")

# 2. *args
print(f"Multiplying numbers: {multiply_all(2, 3, 4)}")

# 3. **kwargs
print("Profile info:")
print_profile(name="Dana", age=30, city="Tel Aviv")

# 4. Function composition
print(describe_rectangle(5, 8))

# 5. Built-in modules
print(random_circle_area())
print(f"Current time: {current_time()}")
