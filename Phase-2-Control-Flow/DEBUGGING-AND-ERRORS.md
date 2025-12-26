# Phase 2: Debugging Guide & Common Errors

## 🐛 Error #1: IndentationError

### What Causes It?
Missing or inconsistent indentation in if/while/for blocks.

### Example (WRONG):
```python
age = int(input("Enter age: "))
if age >= 18:
print("Adult")  # Missing indentation!
```

### Error Message:
```
IndentationError: expected an indented block
```

### Fix:
```python
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")  # Proper indentation
```

### Prevention:
- Use 4 spaces (or 1 tab) consistently
- Enable VS Code indent guide
- Don't mix spaces and tabs

---

## 🐛 Error #2: Infinite Loop

### What Causes It?
Loop condition never becomes False.

### Example (WRONG):
```python
while True:
    age = int(input("Age: "))
    if age >= 18:
        print("Adult")
    # Missing break!
```

### How to Stop:
- Press `Ctrl+C` in terminal
- Program will display: `KeyboardInterrupt`

### Fix:
```python
while True:
    age = int(input("Age: "))
    if age >= 18:
        print("Adult")
        break  # Exit loop
```

### Prevention:
- Always have an exit condition
- Use `break` statements
- Check loop variable updates

---

## 🐛 Error #3: Logic Error (No SyntaxError)

### What Causes It?
Code runs but doesn't do what you expect.

### Example 1 (Wrong Comparison):
```python
age = 17
if age = 18:  # Using = instead of ==
    print("Adult")
# Error: SyntaxError: invalid syntax
```

### Example 2 (Wrong Operator):
```python
age = 17
if age >= 18:  # Correct syntax
    print("Adult")  # Never prints because age < 18
else:
    print("Child")  # Prints
```

### Debug Steps:
1. Add print statements: `print(f"age = {age}")`
2. Check condition: `print(f"age >= 18 is {age >= 18}")`
3. Verify logic is what you intended

### Common Logic Errors:
```python
# Wrong: checking < instead of >
if age < 18:  # WRONG for adult check
    print("Adult")

# Right:
if age >= 18:  # CORRECT
    print("Adult")
```

---

## 🐛 Error #4: Off-by-One with range()

### What Causes It?
Misunderstanding range(start, stop, step).

### Example (WRONG):
```python
# Want 1 to 5
for i in range(5):  # Actually 0 to 4!
    print(i)
# Output: 0, 1, 2, 3, 4  (missing 5)
```

### Correct:
```python
for i in range(1, 6):  # 1 to 5 (stop is exclusive!)
    print(i)
# Output: 1, 2, 3, 4, 5  ✓
```

### Remember:
- `range(n)` → 0 to n-1
- `range(a, b)` → a to b-1 (stop is EXCLUSIVE)
- `range(a, b, step)` → a to b-1, incrementing by step

### Prevention:
- Test with simple examples first
- Print range to verify: `list(range(1, 6))`
- Remember: stop is EXCLUSIVE

---

## 🐛 Error #5: break/continue Outside Loop

### What Causes It?
Using break or continue without being in a loop.

### Example (WRONG):
```python
age = 17
if age < 18:
    break  # ERROR! Not in a loop!
```

### Error Message:
```
SyntaxError: 'break' outside loop
```

### Correct Usage:
```python
while True:
    age = int(input("Age: "))
    if age < 18:
        continue  # Skip this iteration
    else:
        break  # Exit loop
```

---

## 🐛 Error #6: UnboundLocalError

### What Causes It?
Variable used before it's defined.

### Example (WRONG):
```python
count = 0
while count < 5:
    if count == 3:
        count = count + 1  # OK
    print(count)
# But if you use count before initializing:
while count < 5:  # ERROR if count doesn't exist!
    count = count + 1
```

### Fix:
```python
count = 0  # Initialize BEFORE loop
while count < 5:
    print(count)
    count = count + 1
```

---

## 🐛 Error #7: Comparison Always True/False

### What Causes It?
Condition written incorrectly.

### Example:
```python
# WRONG: condition always true
age = 5
if age >= 0:  # Always true for any age!
    print("Valid age")

# WRONG: Using and incorrectly
if age >= 0 and age >= 18:  # Confusing!
    print("Adult")

# RIGHT:
if age >= 18:
    print("Adult")
```

### Debug:
```python
age = 17
print(age >= 18)  # False
print(age < 18)   # True
print(age == 18)  # False
```

---

## 🐛 Debugging Techniques

### 1. Print Debugging
```python
age = int(input("Age: "))
print(f"DEBUG: age = {age}, type = {type(age)}")
if age >= 18:
    print("Adult")
```

### 2. Step Through Code
Add prints after each step:
```python
attempts = 0
while attempts < 3:
    print(f"Attempt {attempts + 1}")  # Debug
    password = input("Password: ")
    print(f"You entered: {password}")  # Debug
    if password == "correct":
        print("Success!")
        break
    attempts += 1
    print(f"Attempts left: {3 - attempts}")  # Debug
```

### 3. Check Variable Types
```python
input_value = input("Number: ")
print(type(input_value))  # <class 'str'>
num = int(input_value)
print(type(num))  # <class 'int'>
```

### 4. Test Conditions Separately
```python
age = 17
print(f"age >= 18: {age >= 18}")  # False
print(f"age < 18: {age < 18}")    # True
print(f"age == 18: {age == 18}")  # False
```

---

## ✅ Testing Checklist

Before submitting code, test:

- [ ] Program runs without IndentationError
- [ ] Infinite loops fixed (using break)
- [ ] Logic correct (test with multiple inputs)
- [ ] range() uses correct start/stop values
- [ ] break/continue only inside loops
- [ ] All variables initialized before use
- [ ] Conditions tested (print to verify)
- [ ] Edge cases tested (0, negative, large numbers)

---

## 📞 Need Help?

If still stuck:
1. Copy the error message
2. Search "Python [error message]"
3. Look for similar problems on StackOverflow
4. Ask your instructor

*Last Updated: December 2024*
