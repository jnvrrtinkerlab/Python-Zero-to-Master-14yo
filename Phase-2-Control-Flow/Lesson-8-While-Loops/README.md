# Lesson 8: While Loops

## Objectives
- Understand how while loops repeat code
- Create loops that run until conditions change
- Avoid infinite loops
- Use break to exit loops early

## What You'll Learn
1. **While Loop Syntax** - Repeat code while condition is TRUE
2. **Loop Counter** - Variable that changes each iteration
3. **Infinite Loops** - When condition never becomes FALSE
4. **Break Keyword** - Exit loop early when needed

## Theory

```python
while condition:
    # Code repeats while condition is TRUE
    # Update condition eventually
```

## Code Examples

### Example 1: Countdown
```python
num = 5
while num > 0:
    print(num)
    num -= 1
print("Done!")
```

### Example 2: Input Validation
```python
while True:
    age = int(input("Enter age: "))
    if 1 <= age <= 120:
        print("Valid!")
        break
    print("Try again")
```

### Example 3: Sum Until Zero
```python
total = 0
while True:
    num = int(input("Enter number (0 to exit): "))
    if num == 0:
        break
    total += num
print(f"Sum: {total}")
```

### Example 4: Password Retry (3 attempts)
```python
password = "python123"
attempts = 0
while attempts < 3:
    user = input("Password: ")
    if user == password:
        print("Access granted!")
        break
    attempts += 1
```

### Example 5: Menu Loop
```python
while True:
    print("\n1. Say Hello\n2. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        break
```

## Common Mistakes
- Forgetting to update the loop variable
- Creating infinite loops accidentally
- Not using break when needed

## Exercises
1. Countdown from 10 to 1
2. Multiplication table
3. Guessing game (with retries)
4. Sum calculator
5. Menu-driven calculator

---

*Last Updated: December 2024*
