# Lesson 6: If/Else Statements

## 📌 Objectives
By the end of this lesson, you will:
- Understand how to make decisions in code using `if` statements
- Write simple `if` and `else` blocks
- Use comparison operators correctly
- Build programs that respond to different conditions

## 📚 Prerequisites
- Lesson 1-5 (Python Basics completed)
- Understanding of variables and data types
- Comfort with print statements and user input

---

## 🎯 What You'll Learn

### Key Concepts:
1. **If Statements** - Execute code when a condition is TRUE
2. **Else Statements** - Execute code when the condition is FALSE
3. **Comparison Operators** - `>`, `<`, `>=`, `<=`, `==`, `!=`
4. **Indentation** - Critical for Python code blocks
5. **Boolean Values** - TRUE and FALSE

---

## 📖 Theory & Explanation

### What is an If/Else Statement?

An **if/else statement** allows your program to make decisions. It checks a condition and:
- **If TRUE**: Executes one block of code
- **If FALSE**: Executes another block of code (optional else)

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|----------|
| `==` | Equal to | `age == 18` |
| `!=` | Not equal to | `name != "Admin"` |
| `>` | Greater than | `marks > 50` |
| `<` | Less than | `marks < 100` |
| `>=` | Greater than or equal | `age >= 18` |
| `<=` | Less than or equal | `age <= 65` |

### Syntax:

```python
if condition:
    # Code runs if condition is TRUE
    # Code is indented (4 spaces or 1 tab)
else:
    # Code runs if condition is FALSE
    # Also indented
```

**IMPORTANT**: Python uses **indentation** (spacing) to show code blocks!

---

## 💡 Code Examples

### Example 1: Simple Age Check

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote! 🗳️")
else:
    print("You must be 18 to vote.")
```

**How it works:**
1. Ask user for their age
2. Check if age is 18 or more
3. If TRUE → Print voting message
4. If FALSE → Print ineligible message

### Example 2: Password Checker

```python
password = input("Enter your password: ")
correct_password = "python123"

if password == correct_password:
    print("Welcome! Access granted! ✅")
else:
    print("Wrong password! Try again. ❌")
```

### Example 3: Grade Checker (Simple)

```python
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("You PASSED! 🎉")
else:
    print("You FAILED! Try again next time.")
```

### Example 4: Even or Odd Number

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")
```

**Explanation**: `%` is the modulo operator (gives remainder)

### Example 5: Temperature Alert

```python
temp = int(input("Enter temperature in °C: "))

if temp > 40:
    print("🔥 VERY HOT! Drink water and stay indoors.")
else:
    print("✅ Temperature is normal.")
```

---

## ⚠️ Common Mistakes

### Mistake 1: Using `=` instead of `==`
```python
# ❌ WRONG
if age = 18:
    print("You are 18")

# ✅ CORRECT
if age == 18:
    print("You are 18")
```

### Mistake 2: Forgetting the colon `:`
```python
# ❌ WRONG
if age >= 18
    print("Adult")

# ✅ CORRECT
if age >= 18:
    print("Adult")
```

### Mistake 3: Wrong indentation
```python
# ❌ WRONG (indentation error)
if age >= 18:
print("Adult")  # Not indented!

# ✅ CORRECT
if age >= 18:
    print("Adult")  # Properly indented
```

### Mistake 4: Using `True/False` instead of condition
```python
# ❌ WRONG
if True:  # Always runs!
    print("Always executes")

# ✅ CORRECT
if age >= 18:  # Actual condition
    print("Adult")
```

---

## 🏋️ Exercises

### Exercise 1: Login System
Create a program that:
- Asks for username
- Asks for password
- Checks if both match (username: "student", password: "learn2024")
- Print success or failure message

### Exercise 2: Discount Calculator
Create a program that:
- Asks for purchase amount
- If amount > 1000, give 10% discount
- Otherwise, no discount
- Show final amount

### Exercise 3: Speed Check
Create a program that:
- Asks for vehicle speed
- If speed > 80 km/h: Print "Speed limit exceeded! Pay fine!"
- Otherwise: Print "Speed is within limit. Drive safely!"

### Exercise 4: Age Category
Create a program that:
- Asks for age
- If age < 13: Print "You are a CHILD"
- Otherwise: Print "You are a TEENAGER or ADULT"

### Exercise 5: Fruit Quality Check
Create a program that:
- Asks for fruit color
- If color is "red": Print "Fruit is ripe! Buy it!"
- If color is "green": Print "Fruit is not ripe. Wait."

---

## 📁 Files in This Lesson

- `README.md` - This file (theory & examples)
- `01_simple_if_else.py` - Basic if/else examples
- `02_age_checker.py` - Age verification program
- `03_password_validator.py` - Password checking
- `04_number_classifier.py` - Even/odd checker
- `05_temperature_alert.py` - Temperature checking
- `solutions/` - Solutions to all exercises

---

## 🎓 Key Takeaways

✅ **If/Else statements make decisions based on conditions**
✅ **Use `==` to compare, `=` to assign values**
✅ **Always use indentation (4 spaces) after colon**
✅ **Comparison operators return True or False**
✅ **Else block is optional**

---

## 🚀 Next Steps

1. Type out all examples yourself
2. Complete all 5 exercises
3. Experiment and modify the code
4. Move to Lesson 7: If/Elif/Else for handling multiple conditions

---

*Last Updated: December 2024*
