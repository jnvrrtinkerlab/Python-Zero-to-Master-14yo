Phase-1-Basics/Lesson-5-CircleAreaProject/README.md# Lesson 5: Circle Area Calculator Project

## Project Goal

Create your first complete program that calculates the area of a circle using the formula:

**Area = π × r²**

where `r` is the radius.

This project combines everything from Lessons 1-4!

---

## What You'll Learn

✅ How to import libraries (math module)
✅ Getting user input
✅ Converting input to numbers
✅ Using mathematical formulas in code
✅ Displaying formatted results

---

## Step-by-Step Solution

### Step 1: Import the Math Library

We need π (pi) from the math library:

```python
import math
```

### Step 2: Get User Input

Ask the user for the radius:

```python
radius = float(input("Enter the radius of the circle: "))
```

**Why `float()`?**
- Radius might be a decimal like 5.5
- `float()` converts text to a decimal number

### Step 3: Calculate the Area

Use the formula A = π × r²:

```python
area = math.pi * (radius ** 2)
```

**Breaking it down:**
- `math.pi` = the value of π (3.14159...)
- `radius ** 2` = radius to the power of 2
- `*` = multiplication

### Step 4: Display the Result

Show the answer nicely:

```python
print(f"Radius: {radius}")
print(f"Area of circle: {area:.2f}")
```

**What's `:.2f`?**
- `.2f` = show 2 decimal places
- Makes the output look clean

---

## Complete Program

```python
# Circle Area Calculator
# This program calculates the area of a circle

import math

print("=== Circle Area Calculator ===")
print()

# Get input from user
radius = float(input("Enter the radius of the circle: "))

# Calculate area using formula: A = π * r²
area = math.pi * (radius ** 2)

# Display results
print()
print("=== Results ===")
print(f"Radius: {radius} cm")
print(f"Area: {area:.2f} cm²")
print()
print(f"The area of a circle with radius {radius} is {area:.2f}")
```

---

## Sample Output

```
=== Circle Area Calculator ===

Enter the radius of the circle: 5

=== Results ===
Radius: 5.0 cm
Area: 78.54 cm²

The area of a circle with radius 5 is 78.54
```

---

## Testing Your Program

Test with these values:

| Radius | Expected Area | Formula |
|--------|---------------|----------|
| 1 | 3.14 | π × 1² = 3.14 |
| 2 | 12.57 | π × 4 = 12.57 |
| 5 | 78.54 | π × 25 = 78.54 |
| 10 | 314.16 | π × 100 = 314.16 |

---

## Enhancements

Once your program works, try these additions:

### Add Circumference Calculation
```python
# Circumference = 2 * π * r
circumference = 2 * math.pi * radius
print(f"Circumference: {circumference:.2f} cm")
```

### Add Error Handling
```python
if radius < 0:
    print("Error! Radius cannot be negative!")
else:
    # calculate and display
```

### Calculate Multiple Circles
```python
for i in range(3):
    r = float(input(f"Enter radius {i+1}: "))
    a = math.pi * (r ** 2)
    print(f"Area: {a:.2f}")
```

---

## Common Issues

### ❌ "math is not defined"
- **Fix:** Make sure you have `import math` at the top!

### ❌ "float() argument must be a string"
- **Fix:** Make sure user enters a number, not text

### ❌ Wrong calculation
- **Check:** Did you use `**` for power, not `^`?
- Python uses `**` for exponentiation!

---

## Challenge Extensions

1. **Calculate a sphere's volume:**
   - Volume = (4/3) × π × r³

2. **Ask for diameter instead:**
   - radius = diameter / 2

3. **Save results to a file:**
   - Write calculations to a text file

4. **Create multiple shapes:**
   - Calculate area for rectangles, triangles, etc.

---

## Key Takeaways

✍️ You can import Python libraries with `import`
✍️ The `math` module has useful constants like `math.pi`
✍️ Use `**` for exponentiation (power)
✍️ F-strings with `:.2f` format numbers nicely
✍️ Always test with known values
✍️ Comments explain what your code does

---

## You've Completed Phase 1! 🎉

You've learned:
- Variables & printing
- Data types
- Operators
- User input
- **And built your first real program!**

**Next Phase: Control Flow (If/Else, Loops)**

You'll learn how to make decisions and repeat code!
