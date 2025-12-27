"""
Lesson 11: Introduction to Functions - Examples
Demonstrating basic function concepts and usage
"""

# ==============================================================================
# EXAMPLE 1: Simple Function with No Parameters
# ==============================================================================

def greet():
    """A simple function that prints a greeting."""
    print("Hello, welcome to Functions!")

# Call the function
greet()


# ==============================================================================
# EXAMPLE 2: Function with Parameters (Arguments)
# ==============================================================================

def greet_person(name):
    """Greet a specific person by name."""
    print(f"Hello, {name}!")

# Call with different arguments
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")


# ==============================================================================
# EXAMPLE 3: Function with Return Value
# ==============================================================================

def add_numbers(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result

# Use the return value
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 20)
print(f"5 + 3 = {sum1}")
print(f"10 + 20 = {sum2}")


# ==============================================================================
# EXAMPLE 4: Function with Multiple Parameters
# ==============================================================================

def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Test with different values
area1 = calculate_area(5, 4)
area2 = calculate_area(10, 7)
print(f"Area of 5x4 rectangle: {area1}")
print(f"Area of 10x7 rectangle: {area2}")


# ==============================================================================
# EXAMPLE 5: Function Performing Calculations
# ==============================================================================

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")


# ==============================================================================
# EXAMPLE 6: Function Creating a String
# ==============================================================================

def create_greeting(name, age):
    """Create a greeting message with name and age."""
    message = f"{name} is {age} years old."
    return message

greeting = create_greeting("Sarah", 16)
print(greeting)


# ==============================================================================
# EXAMPLE 7: Function with Multiple Return Values
# ==============================================================================

def get_student_info(name):
    """Return student information."""
    age = 15
    grade = "9th"
    return name, age, grade

student_name, student_age, student_grade = get_student_info("John")
print(f"Name: {student_name}, Age: {student_age}, Grade: {student_grade}")


# ==============================================================================
# EXAMPLE 8: Function with Repetitive Logic
# ==============================================================================

def print_square(size):
    """Print a square pattern of given size."""
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        print()  # New line after each row

print("\n3x3 Square:")
print_square(3)
print("\n5x5 Square:")
print_square(5)


# ==============================================================================
# EXAMPLE 9: Function that Calls Another Function
# ==============================================================================

def square_number(num):
    """Square a number."""
    return num * num

def sum_of_squares(a, b):
    """Return sum of squares of two numbers."""
    return square_number(a) + square_number(b)

result = sum_of_squares(3, 4)
print(f"\nSum of squares of 3 and 4: {result}")


# ==============================================================================
# EXAMPLE 10: Function for Code Reusability
# ==============================================================================

def check_age_group(age):
    """Determine age group based on age."""
    if age < 13:
        return "Child"
    elif age < 18:
        return "Teen"
    else:
        return "Adult"

ages = [5, 15, 25, 12]
print("\nAge Groups:")
for age in ages:
    group = check_age_group(age)
    print(f"Age {age}: {group}")


print("\n=== All examples completed successfully! ===")
