"""Lesson 9: For Loops - Code Examples

This file demonstrates various for loop patterns and use cases.
"""

# Example 1: Count from 1 to 5
print("=== Example 1: Simple Range Loop ===")
for num in range(1, 6):
    print(num, end=" ")
print()

# Example 2: Loop Through a List
print("\n=== Example 2: Loop Through List ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 3: String Iteration
print("\n=== Example 3: Loop Through String ===")
text = "Python"
for letter in text:
    print(letter, end=" ")
print()

# Example 4: Multiplication Table
print("\n=== Example 4: Multiplication Table (7) ===")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# Example 5: Sum Numbers 1 to 10
print("\n=== Example 5: Sum Numbers ===")
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1 to 10: {total}")

# Example 6: Even Numbers
print("\n=== Example 6: Even Numbers ===")
for num in range(2, 21, 2):
    print(num, end=" ")
print()

# Example 7: Nested Loops
print("\n=== Example 7: Nested Loops (Times Table) ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:3}", end=" ")
    print()

# Example 8: Loop with Break
print("\n=== Example 8: Break Statement ===")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print()

# Example 9: Loop with Continue
print("\n=== Example 9: Continue Statement ===")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print()

# Example 10: Enumerate
print("\n=== Example 10: Using Enumerate ===")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

print("\nAll examples completed!")
