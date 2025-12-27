"""
Lesson 7: If/Elif/Else Logic - Multiple Condition Handling
"""

# EXAMPLE 1: Grade assignment with elif
score = 78
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'  # Output
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Score: {score}, Grade: {grade}")

# EXAMPLE 2: Traffic light system
light = "yellow"
if light == "red":
    action = "STOP"
elif light == "yellow":
    action = "CAUTION"  # Output
elif light == "green":
    action = "GO"
else:
    action = "Unknown"
print(f"Light: {light}, Action: {action}")

# EXAMPLE 3: BMI calculator
weight = 70
height = 1.75
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"  # Output
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"BMI: {bmi:.1f} - {category}")

# EXAMPLE 4: Age-based movie rating
age = 15
if age >= 18:
    rating = "R-rated"
elif age >= 13:
    rating = "PG-13"  # Output
elif age >= 6:
    rating = "PG"
else:
    rating = "G"
print(f"Age {age}: Can watch {rating}")

# EXAMPLE 5: Temperature with nested if
temp = 5
if temp < 0:
    season_action = "Freezing!"
elif temp < 15:
    season_action = "Wear jacket"  # Output
elif temp < 25:
    season_action = "Normal"
else:
    season_action = "Hot"
print(f"Temp {temp}: {season_action}")

# EXAMPLE 6: Day of week
day_num = 3
if day_num == 1:
    day = "Monday"
elif day_num == 2:
    day = "Tuesday"
elif day_num == 3:
    day = "Wednesday"  # Output
elif day_num == 4:
    day = "Thursday"
elif day_num == 5:
    day = "Friday"
elif day_num == 6:
    day = "Saturday"
elif day_num == 7:
    day = "Sunday"
else:
    day = "Invalid"
print(f"Day {day_num}: {day}")

# EXAMPLE 7: Nested if/elif
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")  # Output
    else:
        print("You need a license")
else:
    print("Too young")

# EXAMPLE 8: School fee discount
gpa = 3.8
if gpa >= 3.9:
    discount = 20
elif gpa >= 3.5:
    discount = 15
elif gpa >= 3.0:
    discount = 10
else:
    discount = 0
final_fee = 10000 * (1 - discount/100)
print(f"Discount: {discount}% , Final fee: {final_fee}")

# EXAMPLE 9: Order status
status = "shipped"
if status == "pending":
    msg = "Processing"
elif status == "confirmed":
    msg = "Confirmed"
elif status == "shipped":
    msg = "On the way"  # Output
elif status == "delivered":
    msg = "Delivered"
else:
    msg = "Unknown"
print(f"Status: {msg}")

# EXAMPLE 10: Complex conditions with AND/OR
age = 25
income = 50000
if (age >= 21 and income >= 30000) or (age >= 25):
    loan_eligible = True  # Output
else:
    loan_eligible = False
print(f"Loan Eligible: {loan_eligible}")
