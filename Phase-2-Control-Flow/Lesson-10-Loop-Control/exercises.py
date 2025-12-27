"""Lesson 10: Loop Control (Break & Continue) - Practice Exercises

Solve these exercises to practice break and continue statements.
"""

# Exercise 1: Break at specific number
print("=== Exercise 1: Break at 7 ===")
for i in range(1, 11):
    if i == 7:
        break
    print(i, end=" ")
print("\nBreak at 7!\n")

# Exercise 2: Continue to skip even numbers
print("=== Exercise 2: Skip Even Numbers ===")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n")

# Exercise 3: Find first match
print("=== Exercise 3: Find First Match ===")
names = ["Alice", "Bob", "Charlie", "David"]
target = "Charlie"
for name in names:
    if name == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found")
print()

# Exercise 4: Sum until negative
print("=== Exercise 4: Sum Until Negative ===")
total = 0
while True:
    num_str = input("Enter a positive number (-1 to stop): ")
    num = int(num_str)
    if num < 0:
        break
    total += num
print(f"Total sum: {total}\n")

# Exercise 5: Skip multiples
print("=== Exercise 5: Skip Multiples of 3 ===")
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print("\n")

# Exercise 6: Counter with continue
print("=== Exercise 6: Count Valid Numbers ===")
count = 0
for i in range(1, 21):
    if i % 5 == 0:
        continue
    count += 1
print(f"Numbers from 1-20 (excluding multiples of 5): {count}\n")

# Exercise 7: Password retry
print("=== Exercise 7: Password Validation ===")
password = "python123"
while True:
    attempt = input("Enter password (or 'quit' to exit): ")
    if attempt == "quit":
        break
    if attempt == password:
        print("Correct!")
        break
    print("Wrong! Try again.")
print()

# Exercise 8: Menu loop with break
print("=== Exercise 8: Menu Loop ===")
while True:
    print("1. Start")
    print("2. Settings")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == "3":
        print("Goodbye!")
        break
    elif choice == "1":
        print("Starting...")
    elif choice == "2":
        print("Opening settings...")
    else:
        print("Invalid choice")
print()

# Exercise 9: Pattern with break
print("=== Exercise 9: Break Pattern ===")
for i in range(1, 6):
    for j in range(1, 6):
        if j == 3:
            break
        print(f"{i}{j}", end=" ")
    print()

print()

# Exercise 10: Counter with conditions
print("=== Exercise 10: Count Specific Numbers ===")
count = 0
for i in range(1, 31):
    if i % 2 == 0 and i % 3 == 0:
        count += 1
    elif i % 2 != 0:
        continue
print(f"Numbers divisible by both 2 and 3 from 1-30: {count}")

print("\n=== All Exercises Completed! ===")
