"""
Lesson 6: If/Else Statements - Practice Exercises
Solve these problems to master conditional statements
"""

# ============================================================================
# EXERCISE 1: Check if a number is positive
# ============================================================================
# TODO: Write code that checks if a number is positive (> 0)
# If positive, print "The number is positive"
# If not positive, print "The number is not positive"

number = 5
if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")


# ============================================================================
# EXERCISE 2: Login system
# ============================================================================
# TODO: Check if username is "student" AND password is "learn2024"
# If correct: print "Login successful! Welcome to Python class!"
# If wrong: print "Login failed! Check your username and password."

username = "student"
password = "learn2024"

if username == "student" and password == "learn2024":
    print("Login successful! Welcome to Python class!")
else:
    print("Login failed! Check your username and password.")


# ============================================================================
# EXERCISE 3: Speed limit checker
# ============================================================================
# TODO: Check vehicle speed. If speed > 80 km/h, it's speeding
# If speeding: print "Speed limit exceeded! Pay fine!"
# If safe: print "Speed is within limit. Drive safely!"

speed = 95

if speed > 80:
    print("Speed limit exceeded! Pay fine!")
else:
    print("Speed is within limit. Drive safely!")


# ============================================================================
# EXERCISE 4: Age category classification
# ============================================================================
# TODO: Classify age as child (< 13) or teenager/adult (>= 13)
# Child: print "You are a CHILD"
# Teenager/Adult: print "You are a TEENAGER or ADULT"

age = 10

if age < 13:
    print("You are a CHILD")
else:
    print("You are a TEENAGER or ADULT")


# ============================================================================
# EXERCISE 5: Fruit color quality check
# ============================================================================
# TODO: Check fruit color to determine ripeness
# Red: print "Fruit is ripe! Buy it!"
# Green: print "Fruit is not ripe. Wait."
# Other colors: print "Unknown color. Check again."

fruit_color = "red"

if fruit_color == "red":
    print("Fruit is ripe! Buy it!")
elif fruit_color == "green":
    print("Fruit is not ripe. Wait.")
else:
    print("Unknown color. Check again.")


# ============================================================================
# EXERCISE 6: Movie ticket eligibility
# ============================================================================
# TODO: Check if person can watch a movie based on age
# Age >= 18: print "You can watch any movie"
# Age >= 13: print "You can watch PG-13 movies"
# Age < 13: print "You can watch G-rated movies only"

viewer_age = 25

if viewer_age >= 18:
    print("You can watch any movie")
else:
    if viewer_age >= 13:
        print("You can watch PG-13 movies")
    else:
        print("You can watch G-rated movies only")


# ============================================================================
# EXERCISE 7: Discount calculator
# ============================================================================
# TODO: If purchase amount > 1000, give 10% discount
# Show: Original amount and final amount after discount

purchase_amount = 1500

if purchase_amount > 1000:
    discount = purchase_amount * 0.10
    final_amount = purchase_amount - discount
    print(f"Original: Rs{purchase_amount}, Final: Rs{final_amount:.2f}")
else:
    print(f"No discount. Total: Rs{purchase_amount}")


# ============================================================================
# EXERCISE 8: Weather recommendation
# ============================================================================
# TODO: Based on temperature, give outfit recommendation
# temp > 30: "Wear light clothes and use sunscreen"
# temp 20-30: "Normal clothing is fine"
# temp < 20: "Wear a jacket or sweater"

temperature = 35

if temperature > 30:
    print("Wear light clothes and use sunscreen")
else:
    if temperature >= 20:
        print("Normal clothing is fine")
    else:
        print("Wear a jacket or sweater")


# ============================================================================
# EXERCISE 9: Bank balance check
# ============================================================================
# TODO: Check if account balance is sufficient for withdrawal
# If balance >= withdrawal amount: "Transaction successful"
# If balance < withdrawal amount: "Insufficient funds"

balance = 5000
withdrawal_amount = 6000

if balance >= withdrawal_amount:
    print("Transaction successful")
else:
    print("Insufficient funds")


# ============================================================================
# EXERCISE 10: Test score evaluation
# ============================================================================
# TODO: Check if student passed (score >= 40)
# Pass: print "Congratulations! You passed!"
# Fail: print "You need to study more. Try again!"

test_score = 38

if test_score >= 40:
    print("Congratulations! You passed!")
else:
    print("You need to study more. Try again!")
