"""Lesson 8: While Loops - Practice Exercises

Solve these exercises to practice while loops.
"""

# Exercise 1: Countdown from 10 to 1
print("=== Exercise 1: Countdown ===")
print("Write a program that counts down from 10 to 1")
print("Expected Output: 10 9 8 7 6 5 4 3 2 1")
print()

# Solution:
num = 10
while num >= 1:
    print(num, end=" ")
    num -= 1
print()

# Exercise 2: Multiplication Table
print("\n=== Exercise 2: Multiplication Table ===")
print("Write a program to display the multiplication table of 5")
print("Expected Output: 5 10 15 20 25 30 35 40 45 50")
print()

# Solution:
i = 1
while i <= 10:
    print(5 * i, end=" ")
    i += 1
print()

# Exercise 3: Sum of Numbers
print("\n=== Exercise 3: Sum Numbers 1 to 5 ===")
print("Write a program to find the sum of numbers from 1 to 5")
print("Expected Output: Sum = 15")
print()

# Solution:
total = 0
num = 1
while num <= 5:
    total += num
    num += 1
print(f"Sum = {total}")

# Exercise 4: Print Even Numbers
print("\n=== Exercise 4: Even Numbers from 2 to 20 ===")
print("Write a program to print even numbers from 2 to 20")
print("Expected Output: 2 4 6 8 10 12 14 16 18 20")
print()

# Solution:
num = 2
while num <= 20:
    print(num, end=" ")
    num += 2
print()

# Exercise 5: Guessing Game
print("\n=== Exercise 5: Simple Guessing Game ===")
print("The secret number is 7. Try to guess it!")
print()

# Solution:
secret = 7
guess = -1
while guess != secret:
    try:
        guess = int(input("Guess a number: "))
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print("Correct! You found it!")
    except ValueError:
        print("Please enter a valid number.")

# Exercise 6: Print Odd Numbers
print("\n=== Exercise 6: Odd Numbers from 1 to 19 ===")
print("Write a program to print odd numbers from 1 to 19")
print("Expected Output: 1 3 5 7 9 11 13 15 17 19")
print()

# Solution:
num = 1
while num <= 19:
    print(num, end=" ")
    num += 2
print()

# Exercise 7: Repeat Input Until Valid
print("\n=== Exercise 7: Input Validation ===")
print("Ask user for their favorite color (must be at least 3 characters)")
print()

# Solution:
color = ""
while len(color) < 3:
    color = input("Enter your favorite color (min 3 characters): ")
    if len(color) < 3:
        print("Too short! Please enter at least 3 characters.")

print(f"Your favorite color is: {color}")

# Exercise 8: Count Backwards by 5
print("\n=== Exercise 8: Countdown by 5 ===")
print("Count down from 50 to 0, stepping by 5")
print("Expected Output: 50 45 40 35 30 25 20 15 10 5 0")
print()

# Solution:
num = 50
while num >= 0:
    print(num, end=" ")
    num -= 5
print()

print("\n=== All Exercises Completed! ===")
