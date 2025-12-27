"""Lesson 8: While Loops - Code Examples

This file demonstrates various while loop patterns and use cases.
"""

# Example 1: Simple Countdown
print("=== Example 1: Countdown ===")
num = 5
while num > 0:
    print(num)
    num -= 1
print("Done!\n")

# Example 2: Sum Numbers Until Zero
print("=== Example 2: Sum Until Zero ===")
total = 0
while True:
    user_input = input("Enter a number (0 to stop): ")
    num = int(user_input)
    if num == 0:
        break
    total += num
print(f"Total sum: {total}\n")

# Example 3: Input Validation
print("=== Example 3: Input Validation ===")
while True:
    age = int(input("Enter your age (1-120): "))
    if 1 <= age <= 120:
        print(f"Valid age: {age}")
        break
    print("Invalid age. Try again.\n")

# Example 4: Multiplication Table
print("\n=== Example 4: Multiplication Table ===")
num = int(input("Enter a number for multiplication table: "))
counter = 1
while counter <= 10:
    print(f"{num} x {counter} = {num * counter}")
    counter += 1

# Example 5: Password Attempt Limit
print("\n=== Example 5: Password Retry (3 attempts) ===")
correct_password = "python123"
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    attempts += 1
    print(f"Wrong password. Attempts left: {3 - attempts}")

if attempts == 3:
    print("Account locked!\n")

print("Examples completed!")
