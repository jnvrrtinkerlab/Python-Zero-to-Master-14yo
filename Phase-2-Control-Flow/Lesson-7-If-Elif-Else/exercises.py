"""
Lesson 7: If/Elif/Else Logic - Practice Exercises
Master handling multiple conditions with elif statements
"""

# EXERCISE 1: Grade assignment
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
print(f"Score {score}: Grade {grade}")

# EXERCISE 2: Traffic light system
light = "yellow"
if light == "red":
    action = "STOP"
elif light == "yellow":
    action = "CAUTION"  # Output
elif light == "green":
    action = "GO"
else:
    action = "Invalid"
print(f"Light {light}: {action}")

# EXERCISE 3: Age-based movie rating
age = 15
if age >= 18:
    rating = "R-rated allowed"
elif age >= 13:
    rating = "PG-13 allowed"  # Output
elif age >= 6:
    rating = "PG allowed"
else:
    rating = "G rated only"
print(f"Age {age}: {rating}")

# EXERCISE 4: Temperature categories
temp = 5
if temp < 0:
    category = "Freezing"
elif temp < 15:
    category = "Cold"  # Output
elif temp < 25:
    category = "Normal"
else:
    category = "Hot"
print(f"Temperature {temp}: {category}")

# EXERCISE 5: Day name from number
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
print(f"Day {day_num} is {day}")

# EXERCISE 6: BMI calculator
weight = 70
height = 1.75
bmi = weight / (height ** 2)

if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal"  # Output
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"
print(f"BMI {bmi:.1f}: {bmi_category}")

# EXERCISE 7: Discount based on amount
amount = 1500
if amount > 5000:
    discount = 0.20
elif amount > 1000:
    discount = 0.10  # Output
elif amount > 500:
    discount = 0.05
else:
    discount = 0
final = amount * (1 - discount)
print(f"Amount {amount}: Discount {discount*100}%, Final {final}")

# EXERCISE 8: School fee with GPA
gpa = 3.8
if gpa >= 3.9:
    fee_discount = 20
elif gpa >= 3.5:
    fee_discount = 15  # Output
elif gpa >= 3.0:
    fee_discount = 10
else:
    fee_discount = 0
final_fee = 10000 * (1 - fee_discount/100)
print(f"GPA {gpa}: Discount {fee_discount}%, Fee {final_fee}")

# EXERCISE 9: Order status message
status = "shipped"
if status == "pending":
    message = "Processing your order"
elif status == "confirmed":
    message = "Order confirmed"
elif status == "shipped":
    message = "On the way to you"  # Output
elif status == "delivered":
    message = "Delivered"
else:
    message = "Unknown status"
print(f"Status {status}: {message}")

# EXERCISE 10: Loan eligibility with conditions
age = 25
income = 50000
if (age >= 21 and income >= 30000) or (age >= 25):
    eligible = True  # Output
else:
    eligible = False
print(f"Age {age}, Income {income}: Eligible {eligible}")
