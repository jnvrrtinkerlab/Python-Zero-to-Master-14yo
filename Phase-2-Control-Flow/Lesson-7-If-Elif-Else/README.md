# Lesson 7: If/Elif/Else Logic

## Objectives
By the end of this lesson, you will:
- Handle multiple conditions using `elif`
- Design decision trees with multiple branches
- Use logical operators (`and`, `or`, `not`) in conditions

## What You'll Learn

### Key Concepts:
1. **Elif (Else If)** - Check additional conditions
2. **Multiple Branches** - Handle many different cases
3. **Logical Operators** - `and`, `or`, `not`

## Theory & Explanation

### Syntax:
```python
if condition1:
    # Code if condition1 is TRUE
elif condition2:
    # Code if condition1 is FALSE but condition2 is TRUE
else:
    # Code if ALL conditions are FALSE
```

## Code Examples

### Example 1: Grade Based on Marks
```python
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A - Excellent!")
elif marks >= 75:
    print("Grade B - Very Good!")
elif marks >= 60:
    print("Grade C - Good!")
else:
    print("Grade F - Failed")
```

### Example 2: Ticket Pricing
```python
age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age < 12:
    price = 5
else:
    price = 10

print(f"Ticket price: Rs. {price}")
```

### Example 3: Using AND/OR Operators
```python
hour = int(input("Enter hour: "))

if hour >= 5 and hour < 12:
    print("Good Morning!")
elif hour >= 12 and hour < 17:
    print("Good Afternoon!")
else:
    print("Good Night!")
```

## Exercises

1. Grade assignment program (A/B/C/D/F)
2. Restaurant menu selector
3. Weather clothes recommendation
4. BMI calculator
5. Scholarship eligibility checker

---

*Last Updated: December 2024*
