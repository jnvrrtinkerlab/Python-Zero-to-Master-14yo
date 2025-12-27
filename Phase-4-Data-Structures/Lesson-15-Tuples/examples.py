# LESSON 15: Tuples - Examples
# Demonstration of tuple concepts

print("="*50)
print("LESSON 15: Tuples")
print("="*50)

# EXAMPLE 1: Creating Tuples
print("\n--- Example 1: Creating Tuples ---")
empty = ()
colors = ("red", "green", "blue")
numbers = (1, 2, 3, 4, 5)
single = (42,)  # Note the comma
no_parens = 10, 20, 30
mixed = (1, "hello", 3.14, True)

print(f"Empty tuple: {empty}")
print(f"Colors: {colors}")
print(f"Numbers: {numbers}")
print(f"Single element: {single}")
print(f"No parentheses: {no_parens}")
print(f"Mixed types: {mixed}")

# EXAMPLE 2: Indexing and Slicing
print("\n--- Example 2: Indexing and Slicing ---")
fruits = ("apple", "banana", "orange", "mango")
print(f"Fruits: {fruits}")
print(f"First: {fruits[0]}")
print(f"Last: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")
print(f"Reversed: {fruits[::-1]}")

# EXAMPLE 3: Tuple Methods
print("\n--- Example 3: Tuple Methods ---")
values = (1, 2, 3, 2, 4, 2, 5)
print(f"Values: {values}")
print(f"Count of 2: {values.count(2)}")
print(f"Index of 3: {values.index(3)}")
print(f"Tuple length: {len(values)}")

# EXAMPLE 4: Tuple Unpacking
print("\n--- Example 4: Tuple Unpacking ---")
point = (10, 20)
x, y = point
print(f"Point: {point}")
print(f"x={x}, y={y}")

coordinates = (5, 15, 25)
a, b, c = coordinates
print(f"Coordinates: {coordinates}")
print(f"a={a}, b={b}, c={c}")

# EXAMPLE 5: Tuples vs Lists
print("\n--- Example 5: Tuples vs Lists ---")
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

print(f"Tuple: {my_tuple}")
print(f"List: {my_list}")
print(f"Tuple is immutable: {type(my_tuple)}")
print(f"List is mutable: {type(my_list)}")

# Try to modify
try:
    my_tuple[0] = 99
except TypeError as e:
    print(f"Error modifying tuple: Tuples are immutable")

my_list[0] = 99
print(f"Modified list: {my_list}")

# EXAMPLE 6: Tuple as Dictionary Key
print("\n--- Example 6: Tuple as Dictionary Key ---")
locations = {}
locations[(0, 0)] = "Origin"
locations[(10, 20)] = "Point A"
locations[(5, 15)] = "Point B"

for coord, name in locations.items():
    print(f"{coord}: {name}")

# EXAMPLE 7: Multiple Return Values
print("\n--- Example 7: Multiple Return Values ---")
def get_coordinates():
    return (10, 20)

def get_user_info():
    return "Alice", 25, "alice@email.com"

x, y = get_coordinates()
name, age, email = get_user_info()

print(f"Coordinates: {x}, {y}")
print(f"User: {name}, Age: {age}, Email: {email}")

# EXAMPLE 8: Tuple Concatenation
print("\n--- Example 8: Tuple Concatenation ---")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(f"{tuple1} + {tuple2} = {result}")

# EXAMPLE 9: Tuple Repetition
print("\n--- Example 9: Tuple Repetition ---")
pattern = (1, 2)
repeated = pattern * 3
print(f"{pattern} * 3 = {repeated}")

# EXAMPLE 10: Converting Between Lists and Tuples
print("\n--- Example 10: Converting Between Lists and Tuples ---")
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(f"List -> Tuple: {my_list} -> {my_tuple}")

back_to_list = list(my_tuple)
print(f"Tuple -> List: {my_tuple} -> {back_to_list}")

print("\n" + "="*50)
print("Key Points: Tuples are immutable and hashable")
print("="*50)
