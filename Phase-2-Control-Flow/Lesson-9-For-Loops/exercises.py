"""Lesson 9: For Loops - Practice Exercises

Solve these exercises to practice for loops.
"""

# Exercise 1: Numbers 1 to 10
print("=== Exercise 1: Print numbers 1 to 10 ===")
for i in range(1, 11):
    print(i, end=" ")
print()

# Exercise 2: Multiplication Table
print("\n=== Exercise 2: Multiplication Table (3) ===")
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")

# Exercise 3: Sum of numbers 1 to 5
print("\n=== Exercise 3: Sum of numbers 1 to 5 ===")
total = 0
for i in range(1, 6):
    total += i
print(f"Sum = {total}")

# Exercise 4: Loop through a list
print("\n=== Exercise 4: Loop through list ===")
animals = ["cat", "dog", "bird", "fish"]
for animal in animals:
    print(f"Animal: {animal}")

# Exercise 5: Count backwards
print("\n=== Exercise 5: Count backwards from 10 to 1 ===")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Exercise 6: Even numbers from 2 to 20
print("\n=== Exercise 6: Even numbers from 2 to 20 ===")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# Exercise 7: Character count
print("\n=== Exercise 7: Count characters in word ===")
word = "Python"
for i, char in enumerate(word):
    print(f"Position {i}: {char}")

# Exercise 8: Sum of even numbers
print("\n=== Exercise 8: Sum of even numbers (1-10) ===")
even_sum = 0
for i in range(2, 11, 2):
    even_sum += i
print(f"Sum of even numbers: {even_sum}")

# Exercise 9: Nested loop pattern
print("\n=== Exercise 9: Rectangle pattern ===")
for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()

# Exercise 10: Fibonacci sequence
print("\n=== Exercise 10: Fibonacci sequence (first 7) ===")
a, b = 0, 1
for i in range(7):
    print(a, end=" ")
    a, b = b, a + b
print()

print("\n=== All Exercises Completed! ===")
