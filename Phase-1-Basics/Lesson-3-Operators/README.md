Phase-1-Basics/Lesson-3-Operators/README.md# Lesson 3: Basic Operators (+, -, *, /, %, //, **)

## What are Operators?

Operators are symbols that perform actions on variables and values.

Think of them like math symbols:
- **+** is addition
- **-** is subtraction
- **\*** is multiplication

---

## Arithmetic Operators

### 1. Addition (+)
Adds two numbers together.

```python
a = 10
b = 5
print(a + b)  # Output: 15
```

### 2. Subtraction (-)
Subtracts one number from another.

```python
a = 10
b = 5
print(a - b)  # Output: 5
```

### 3. Multiplication (*)
Multiplies two numbers.

```python
a = 10
b = 5
print(a * b)  # Output: 50
```

### 4. Division (/)
Divides one number by another (result is always decimal).

```python
a = 10
b = 4
print(a / b)  # Output: 2.5
```

### 5. Floor Division (//)
Divides and rounds DOWN to nearest whole number.

```python
a = 10
b = 4
print(a // b)  # Output: 2 (not 2.5)
```

### 6. Modulo (%)
Returns the REMAINDER after division.

```python
a = 10
b = 3
print(a % b)  # Output: 1 (10 divided by 3 = 3 remainder 1)
```

**Use modulo to:**
- Check if a number is even or odd
- Find remainders
- Cycle through patterns

### 7. Exponentiation (**)
Raises a number to a power.

```python
a = 2
b = 3
print(a ** b)  # Output: 8 (2^3 = 2*2*2)
```

---

## Order of Operations

Python follows the same order as math (PEMDAS/BODMAS):
1. **()** Parentheses
2. **\*\*** Exponentiation
3. **\*, /, //, %** Multiplication, Division (left to right)
4. **+, -** Addition, Subtraction (left to right)

```python
print(2 + 3 * 4)      # 2 + (3*4) = 14, NOT (2+3)*4
print((2 + 3) * 4)    # (2+3)*4 = 20
print(10 - 3 - 2)     # (10-3)-2 = 5 (left to right)
```

---

## Assignment Operators

Shortcut operators to assign values:

```python
x = 10
x += 5        # Same as x = x + 5, result: 15
x -= 3        # Same as x = x - 3, result: 12
x *= 2        # Same as x = x * 2, result: 24
x /= 4        # Same as x = x / 4, result: 6.0
```

---

## Comparison Operators

Compare two values (result is True or False):

```python
print(10 > 5)      # True (greater than)
print(10 < 5)      # False (less than)
print(10 >= 10)    # True (greater than or equal)
print(10 <= 9)     # False (less than or equal)
print(10 == 10)    # True (equal to)
print(10 != 5)     # True (not equal to)
```

**Important:** Use **==** to compare, NOT **=** (= assigns)

---

## Common Mistakes

```python
print(10 / 3)   # 3.333... (decimal)
print(10 // 3)  # 3 (whole number)
print(2 ** 3)   # 8 (2 to the power of 3)
print(2 * 3)    # 6 (NOT 6 exponentiation)
```

---

## Practical Examples

```python
# Calculate age in days
age_years = 14
days_per_year = 365
age_days = age_years * days_per_year
print(f"You are approximately {age_days} days old!")

# Check if number is even
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Calculate area of a circle
import math
radius = 5
area = math.pi * (radius ** 2)
print(f"Area: {area}")
```

---

## Exercise

Write a program that:
1. Takes two numbers
2. Performs all 7 arithmetic operations
3. Prints the results

```python
a = 20
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
```

---

## Key Points

✍️ Arithmetic operators: +, -, *, /, //, %, **
✍️ Order of operations: Parentheses, Exponents, Multiply/Divide, Add/Subtract
✍️ Use = to assign, == to compare
✍️ // gives whole number, / gives decimal
✍️ % gives remainder
✍️ ** means "to the power of"

---

## Next: Lesson 4 - User Input

Learn how to get information from the user!
