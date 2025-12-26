# Lesson 9: For Loops

## Objectives
- Iterate over ranges and sequences
- Use for loops with range()
- Loop through strings and lists
- Understand loop variable usage

## What You'll Learn
1. **For Loop Syntax** - Iterate for fixed number of times
2. **range() Function** - Generate sequence of numbers
3. **Iterating Strings/Lists** - Loop through characters and items
4. **Loop Variables** - Using counter in iterations

## Theory

```python
for variable in sequence:
    # Code runs for each item
```

## Code Examples

### Example 1: Using range()
```python
for i in range(1, 6):
    print(f"Number: {i}")
# Output: 1, 2, 3, 4, 5
```

### Example 2: Loop Through String
```python
name = "Python"
for char in name:
    print(char)
# Output: P, y, t, h, o, n
```

### Example 3: Multiplication Table
```python
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Example 4: Sum of Numbers
```python
total = 0
for num in range(1, 6):
    total += num
print(f"Sum: {total}")
```

### Example 5: List Processing
```python
students = ["Ali", "Sara", "Khan"]
for name in students:
    print(f"Hello, {name}!")
```

## Common Mistakes
- Off-by-one errors with range()
- Confusing range(n) with range(0, n)
- Modifying list while looping

## Exercises
1. Print 1 to 10
2. Multiplication table
3. Sum of 1 to 100
4. Pattern printer
5. List iterator

---

*Last Updated: December 2024*
