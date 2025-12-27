"""
Lesson 12: Function Parameters and Return Values - Examples
"""

# EXAMPLE 1: Single Parameter and Return
def square(num):
    return num * num

print(f"Square of 5: {square(5)}")
print(f"Square of 10: {square(10)}")


# EXAMPLE 2: Multiple Parameters
def add(a, b):
    result = a + b
    return result

print(f"\nAdd 7 + 3 = {add(7, 3)}")
print(f"Add 100 + 50 = {add(100, 50)}")


# EXAMPLE 3: Multiple Return Values (Tuple)
def get_dimensions():
    width = 10
    height = 20
    return width, height

w, h = get_dimensions()
print(f"\nDimensions: {w} x {h}")


# EXAMPLE 4: Function Using Return Value in Calculation
def multiply(a, b):
    return a * b

def calculate_area_and_perimeter(length, width):
    area = multiply(length, width)
    perimeter = 2 * (length + width)
    return area, perimeter

area, peri = calculate_area_and_perimeter(5, 3)
print(f"\nRectangle 5x3: Area={area}, Perimeter={peri}")


# EXAMPLE 5: Optional Early Return
def validate_age(age):
    if age < 0:
        return False
    if age > 150:
        return False
    return True

print(f"\nAge 25 valid: {validate_age(25)}")
print(f"Age -5 valid: {validate_age(-5)}")


# EXAMPLE 6: Return Complex Objects
def get_student():
    name = "Alice"
    grade = "A"
    score = 95
    return {"name": name, "grade": grade, "score": score}

student = get_student()
print(f"\nStudent: {student}")


# EXAMPLE 7: Chaining Return Values
def process_number(num):
    doubled = num * 2
    return doubled

def add_ten(num):
    return num + 10

result = add_ten(process_number(5))
print(f"\n5 * 2 + 10 = {result}")


# EXAMPLE 8: Parameter Order Matters
def divide(numerator, denominator):
    if denominator == 0:
        return None
    return numerator / denominator

print(f"\n10 / 2 = {divide(10, 2)}")
print(f"2 / 10 = {divide(2, 10)}")


# EXAMPLE 9: Multiple Parameters, Single Return
def calculate_total(price, quantity, tax_rate=0.1):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax

print(f"\nTotal: {calculate_total(10, 5)}")
print(f"Total with 20% tax: {calculate_total(10, 5, 0.2)}")


# EXAMPLE 10: Return None Implicitly
def greet(name):
    print(f"Hello, {name}!")
    # No return statement - returns None

result = greet("Bob")
print(f"Return value of greet: {result}")


print("\n=== Lesson 12 Complete ===")
