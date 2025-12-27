# LESSON 14: Introduction to Lists
# Examples demonstrating list concepts

print("=" * 50)
print("LESSON 14: Introduction to Lists")
print("=" * 50)

# EXAMPLE 1: Creating Lists
print("\n--- Example 1: Creating Lists ---")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with numbers
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# List with strings
fruits = ["apple", "banana", "orange", "mango"]
print(f"Fruits: {fruits}")

# Mixed data types
mixed = [1, "hello", 3.14, True, None]
print(f"Mixed list: {mixed}")

# EXAMPLE 2: List Indexing
print("\n--- Example 2: List Indexing ---")

fruits = ["apple", "banana", "orange", "mango"]

print(f"First fruit (index 0): {fruits[0]}")
print(f"Second fruit (index 1): {fruits[1]}")
print(f"Last fruit (index -1): {fruits[-1]}")
print(f"Second last fruit (index -2): {fruits[-2]}")
print(f"List length: {len(fruits)}")

# EXAMPLE 3: List Slicing
print("\n--- Example 3: List Slicing ---")

numbers = [10, 20, 30, 40, 50, 60]

print(f"Original list: {numbers}")
print(f"Slice [1:3]: {numbers[1:3]}")
print(f"Slice [:3]: {numbers[:3]}")
print(f"Slice [3:]: {numbers[3:]}")
print(f"Slice [::2] (every 2nd element): {numbers[::2]}")
print(f"Slice [::-1] (reversed): {numbers[::-1]}")

# EXAMPLE 4: Adding Elements
print("\n--- Example 4: Adding Elements ---")

fruits = ["apple", "banana"]
print(f"Original: {fruits}")

fruits.append("orange")
print(f"After append('orange'): {fruits}")

fruits.extend(["mango", "grape"])
print(f"After extend(['mango', 'grape']): {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert(1, 'blueberry'): {fruits}")

# EXAMPLE 5: Removing Elements
print("\n--- Example 5: Removing Elements ---")

fruits = ["apple", "banana", "orange", "mango"]
print(f"Original: {fruits}")

fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

removed = fruits.pop()
print(f"After pop(): {fruits}")
print(f"Popped element: {removed}")

removed = fruits.pop(0)
print(f"After pop(0): {fruits}")
print(f"Popped element: {removed}")

# EXAMPLE 6: List Methods
print("\n--- Example 6: List Methods ---")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# Sort
sorted_nums = sorted(numbers)
print(f"sorted(): {sorted_nums}")

# Reverse
reversed_nums = numbers[::-1]
print(f"Reversed (slice): {reversed_nums}")

# Count
count = numbers.count(1)
print(f"Count of 1: {count}")

# Index
index = numbers.index(4)
print(f"Index of 4: {index}")

# EXAMPLE 7: List Iteration
print("\n--- Example 7: List Iteration ---")

fruits = ["apple", "banana", "orange"]

print("Using for loop:")
for fruit in fruits:
    print(f"  - {fruit}")

print("\nUsing enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# EXAMPLE 8: List Comprehension
print("\n--- Example 8: List Comprehension ---")

# Simple list comprehension
squares = [x**2 for x in range(5)]
print(f"Squares of 0-4: {squares}")

# List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers 0-9: {evens}")

# EXAMPLE 9: Common Patterns
print("\n--- Example 9: Common Patterns ---")

scores = [85, 90, 78, 92, 88]

# Sum
total = sum(scores)
print(f"Total score: {total}")

# Average
average = sum(scores) / len(scores)
print(f"Average score: {average:.2f}")

# Max and Min
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")

# EXAMPLE 10: Copying Lists
print("\n--- Example 10: Copying Lists ---")

original = [1, 2, 3]

# Shallow copy
shallow_copy = original.copy()
shallow_copy[0] = 999

print(f"Original: {original}")
print(f"Shallow copy after modification: {shallow_copy}")

print("\n" + "="*50)
print("Review: Key List Concepts")
print("="*50)
print("1. Lists are ordered and mutable")
print("2. Use indexing to access individual elements")
print("3. Use slicing to get subsets")
print("4. Methods: append, extend, insert, remove, pop")
print("5. Iteration with for loops or enumerate")
print("6. List comprehension for creating new lists")
print("="*50)
