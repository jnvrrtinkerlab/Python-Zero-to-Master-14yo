"""
Lesson 6: If/Else Statements - Complete Examples
Learn how programs make decisions using if/else
"""

# ============================================================================
# EXAMPLE 1: Basic if statement - Single decision
# ============================================================================
age = 15

if age >= 13:
    print("You can watch this content")
# Output: You can watch this content


# ============================================================================
# EXAMPLE 2: if with else - Two choices
# ============================================================================
score = 45

if score >= 50:
    print("You passed!")
else:
    print("You failed. Try again!")
# Output: You failed. Try again!


# ============================================================================
# EXAMPLE 3: Comparison operators explained
# ============================================================================
num = 10

# Equal to (==)
if num == 10:
    print("num is exactly 10")  # Output: num is exactly 10

# Not equal to (!=)
if num != 5:
    print("num is not 5")  # Output: num is not 5

# Greater than (>)
if num > 5:
    print("num is greater than 5")  # Output: num is greater than 5

# Less than (<)
if num < 15:
    print("num is less than 15")  # Output: num is less than 15

# Greater than or equal to (>=)
if num >= 10:
    print("num is 10 or more")  # Output: num is 10 or more

# Less than or equal to (<=)
if num <= 20:
    print("num is 20 or less")  # Output: num is 20 or less


# ============================================================================
# EXAMPLE 4: Boolean values (True/False)
# ============================================================================
is_student = True

if is_student:
    print("Get student discount!")  # Output: Get student discount!

is_premium = False

if is_premium:
    print("Access premium features")
else:
    print("Upgrade to premium for more features")
# Output: Upgrade to premium for more features


# ============================================================================
# EXAMPLE 5: String comparison
# ============================================================================
username = "alice"

if username == "alice":
    print("Welcome Alice!")  # Output: Welcome Alice!
else:
    print("Unknown user")


# ============================================================================
# EXAMPLE 6: Practical real-world example - Age verification
# ============================================================================
age_for_movie = 16

if age_for_movie >= 18:
    print("You can watch this R-rated movie")
else:
    print("You're too young. Parental permission needed")
# Output: You're too young. Parental permission needed


# ============================================================================
# EXAMPLE 7: Multiple independent if statements
# ============================================================================
temperature = 28

if temperature > 30:
    print("It's hot! Drink water")

if temperature < 15:
    print("It's cold! Wear a jacket")

if temperature >= 20 and temperature <= 25:
    print("Perfect weather!")
# Output: Perfect weather!


# ============================================================================
# EXAMPLE 8: User input with if/else
# ============================================================================
name = "Bob"

if name == "":
    print("Please enter a name")
else:
    print(f"Hello, {name}!")
# Output: Hello, Bob!


# ============================================================================
# EXAMPLE 9: Number range checking
# ============================================================================
marks = 75

if marks >= 90:
    print("Grade: A")
else:
    if marks >= 80:
        print("Grade: B")
    else:
        if marks >= 70:
            print("Grade: C")  # Output: Grade: C
        else:
            print("Grade: F")


# ============================================================================
# EXAMPLE 10: Indentation matters
# ============================================================================
is_admin = True

if is_admin:
    print("You have admin access")
    print("You can delete files")
    print("Be careful!")

print("Program continues here")
# Output:
# You have admin access
# You can delete files
# Be careful!
# Program continues here
