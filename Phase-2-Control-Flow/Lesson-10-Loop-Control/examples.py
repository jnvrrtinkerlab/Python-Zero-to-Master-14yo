"""Lesson 10: Loop Control (Break & Continue) - Code Examples

This file demonstrates break and continue statements in loops.
"""

# Example 1: Break statement - Exit loop early
print("=== Example 1: Break Statement ===")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print("\n(Loop stopped at 5)\n")

# Example 2: Continue statement - Skip iteration
print("=== Example 2: Continue Statement ===")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print("\n(Skipped 3)\n")

# Example 3: Break with user input
print("=== Example 3: Break with Input ===")
while True:
    user_input = input("Enter a number (0 to exit): ")
    num = int(user_input)
    if num == 0:
        break
    print(f"You entered: {num}")
print("Loop exited!\n")

# Example 4: Continue with condition
print("=== Example 4: Continue Example ===")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"Odd: {i}", end=" ")
print("\n")

# Example 5: Nested loops with break
print("=== Example 5: Nested Loops with Break ===")
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"({i},{j})", end=" ")
    print()

print()

# Example 6: Search and break
print("=== Example 6: Search with Break ===")
fruits = ["apple", "banana", "cherry", "date"]
search = "cherry"
for fruit in fruits:
    if fruit == search:
        print(f"Found {search}!")
        break
else:
    print(f"{search} not found")

print()

# Example 7: Continue in while loop
print("=== Example 7: Continue in While Loop ===")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(f"Number: {i}")

print()

# Example 8: Break with flag
print("=== Example 8: Break with Flag ===")
found = False
for i in range(1, 11):
    if i == 7:
        found = True
        break
if found:
    print("Found the number 7")
else:
    print("Number 7 not found")

print("\nAll examples completed!")
