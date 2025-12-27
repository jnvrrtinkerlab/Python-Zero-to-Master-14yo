# LESSON 15: Tuples - Exercises
# Practice problems for tuple concepts

print("="*60)
print("LESSON 15: Tuples - Practice Exercises")
print("="*60)

# EXERCISE 1: Create Tuples
print("\n--- EXERCISE 1: Create Tuples ---")
print("# TODO: Create the following tuples:")
print("# 1. Empty tuple")
print("# 2. Tuple with 3 colors")
print("# 3. Single element tuple with value 42")
print("# 4. Tuple without parentheses: 10, 20, 30")
print("# Print all tuples")

# EXERCISE 2: Tuple Indexing
print("\n--- EXERCISE 2: Tuple Indexing ---")
students = ("Alice", "Bob", "Charlie", "Diana")
print(f"Students: {students}")
print("# TODO: Print:")
print("# - First student")
print("# - Last student")
print("# - Student at index 2")
print("# - Length of tuple")

# EXERCISE 3: Tuple Slicing
print("\n--- EXERCISE 3: Tuple Slicing ---")
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
print(f"Numbers: {numbers}")
print("# TODO: Extract:")
print("# - First three elements")
print("# - Last three elements")
print("# - Every other element")
print("# - Reversed tuple")

# EXERCISE 4: Tuple Unpacking
print("\n--- EXERCISE 4: Tuple Unpacking ---")
coordinate = (10, 20)
print(f"Coordinate: {coordinate}")
print("# TODO: Unpack into x and y, then print them")

user_info = ("John", 25, "john@email.com")
print(f"User Info: {user_info}")
print("# TODO: Unpack into name, age, email, then print")

# EXERCISE 5: Tuple Methods
print("\n--- EXERCISE 5: Tuple Methods ---")
values = (10, 20, 30, 20, 40, 20, 50)
print(f"Values: {values}")
print("# TODO: Use tuple methods to:")
print("# 1. Count how many times 20 appears")
print("# 2. Find the index of 30")
print("# 3. Find the length")

# EXERCISE 6: Immutability
print("\n--- EXERCISE 6: Immutability ---")
my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple}")
print("# TODO: Try to modify my_tuple[0] = 99")
print("# Expected: TypeError (tuples are immutable)")

# EXERCISE 7: Comparing with Lists
print("\n--- EXERCISE 7: Comparing with Lists ---")
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
print(f"Tuple: {my_tuple}")
print(f"List: {my_list}")
print("# TODO: Explain the difference between them")
print("# - Mutability")
print("# - Use as dictionary keys")
print("# - Performance")

# EXERCISE 8: Tuple Concatenation
print("\n--- EXERCISE 8: Tuple Concatenation ---")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(f"Tuple1: {tuple1}")
print(f"Tuple2: {tuple2}")
print("# TODO: Concatenate them and print result")
print("# TODO: Repeat (1, 2) three times")

# EXERCISE 9: Tuple as Dictionary Key
print("\n--- EXERCISE 9: Tuple as Dictionary Key ---")
print("# TODO: Create a dictionary using coordinates as keys:")
print("# - (0, 0) -> 'Origin'")
print("# - (10, 20) -> 'Point A'")
print("# - (5, 15) -> 'Point B'")
print("# Then iterate and print all entries")

# EXERCISE 10: Working with Tuples
print("\n--- EXERCISE 10: Working with Tuples ---")
print("# TODO: Create a program that:")
print("# 1. Stores RGB color as a tuple (r, g, b)")
print("# 2. Creates multiple colors")
print("# 3. Finds the color with maximum red value")
print("# 4. Prints all colors in reverse order")

print("\n" + "="*60)
print("Challenge: Tuple operations")
print("="*60)
print("Create a function that:")
print("1. Returns a tuple of (sum, average) for a list")
print("2. Unpacks the result in the calling code")
print("3. Test with [10, 20, 30, 40]")
print("="*60)
