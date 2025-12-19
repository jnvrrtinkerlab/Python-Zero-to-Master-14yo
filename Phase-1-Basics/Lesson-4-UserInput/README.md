# Lesson 4: Taking User Input

## What is User Input?

User input is when your program asks the user to type something and uses that information.

Think of it like asking a question:
- "What's your name?" → User types: "Alice"
- Your program stores that answer and uses it

---

## The input() Function

We use `input()` to ask users for information.

```python
name = input("What is your name? ")
print("Hello,", name)
```

**How it works:**
1. Python displays: "What is your name? "
2. User types: "Alice"
3. Python stores it in variable `name`
4. Program says: "Hello, Alice"

---

## Important: input() Returns Text!

Everything from `input()` is a STRING, even numbers!

```python
age = input("How old are you? ")  # User types: 14
print(type(age))                   # <class 'str'> NOT an integer!
```

---

## Converting Input to Numbers

If you need a number, convert it!

### Converting to Integer (int)
```python
age = int(input("How old are you? "))
print(age + 1)  # This works! age is now a number
```

### Converting to Float (float)
```python
height = float(input("How tall are you in feet? "))
print(f"Your height: {height}")
```

---

## Prompts

Always tell users what to type:

```python
# Good prompts
name = input("Enter your name: ")
age = int(input("Enter your age: "))
favorite_subject = input("What's your favorite subject? ")

# Bad prompts (confusing)
name = input("> ")
age = int(input("?"))
```

---

## Complete Program Example

```python
print("=== Student Info Program ===")

# Get student information
name = input("What is your name? ")
age = int(input("How old are you? "))
grade = input("What grade are you in? ")
favorite_subject = input("What's your favorite subject? ")

# Display the information
print("\n=== Your Information ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Grade: {grade}")
print(f"Favorite Subject: {favorite_subject}")
print(f"\nHello {name}! You are {age} years old!")
```

**Output:**
```
=== Student Info Program ===
What is your name? Alice
How old are you? 14
What grade are you in? 9
What's your favorite subject? Math

=== Your Information ===
Name: Alice
Age: 14
Grade: 9
Favorite Subject: Math

Hello Alice! You are 14 years old!
```

---

## Common Mistakes

### ❌ Mistake 1: Forgetting to Convert
```python
age = input("Age: ")      # User types: 14
print(age + 5)           # ERROR! Can't add number to string
```

**Fix:**
```python
age = int(input("Age: ")) # User types: 14
print(age + 5)           # Result: 19 ✅
```

### ❌ Mistake 2: No Prompt
```python
name = input()           # User doesn't know what to type!
```

**Fix:**
```python
name = input("Your name: ") # Clear instruction ✅
```

### ❌ Mistake 3: Not Handling Errors
```python
age = int(input("Age: ")) # If user types "abc", program crashes!
```

---

## Exercise

Create a program that:
1. Asks for the user's name
2. Asks for their favorite color
3. Asks for their favorite number
4. Displays all the information back

**Expected Output Example:**
```
What is your name? Bob
What is your favorite color? Blue
What is your favorite number? 7

Hello Bob!
Your favorite color is Blue
Your favorite number is 7
```

---

## Practice Programs

### Simple Math with User Input
```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
```

### Greeting Program
```python
first_name = input("First name: ")
last_name = input("Last name: ")
print(f"Welcome, {first_name} {last_name}!")
```

---

## Key Points

✍️ `input()` always returns a STRING
✍️ Use `int()` to convert to integer
✍️ Use `float()` to convert to decimal number
✍️ Always provide a clear prompt
✍️ Test your program with different inputs
✍️ f-strings make it easy to display results

---

## Next: Lesson 5 - Circle Area Project

Use everything you've learned to solve a real problem!
