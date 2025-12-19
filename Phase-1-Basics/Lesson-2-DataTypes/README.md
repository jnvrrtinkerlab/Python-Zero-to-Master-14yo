# Lesson 2: Data Types (Numbers, Strings, Booleans)

## What are Data Types?

A **data type** is the kind of data a variable holds. Different types of data require different storage and handling.

Think of it like a container:
- A **bottle** holds liquids (numbers with decimals)
- A **box** holds packages (text/strings)
- A **light switch** is ON or OFF (true/false)

---

## The Main Data Types in Python

### 1. **Integers** (int) - Whole Numbers

Integers are numbers WITHOUT decimal points.

```python
age = 14              # Positive integer
temperature = -5      # Negative integer
count = 0             # Zero
year = 2025           # Large integer
```

**Use integers for:**
- Counting things (students, scores, points)
- Ages, years, dates
- Temperatures

---

### 2. **Floats** (float) - Decimal Numbers

Floats are numbers WITH decimal points.

```python
height = 5.6          # Height in feet
price = 9.99          # Price in dollars
temperature = 36.5    # Body temperature
pi = 3.14159          # Mathematical constant
```

**Use floats for:**
- Measurements (height, weight, distance)
- Money (prices, costs)
- Scientific calculations
- Temperatures

---

### 3. **Strings** (str) - Text

Strings are text enclosed in quotes (single ' or double ").

```python
name = "Alice"                           # Double quotes
city = 'New York'                        # Single quotes
message = "I love Python!"               # Text with spaces
empty_string = ""                        # Empty string
```

**Use strings for:**
- Names, addresses
- Messages, sentences
- Usernames, emails
- Any text data

**Important:** Quotes are REQUIRED for strings!

```python
print("Alice")   # ✅ Correct
print(Alice)     # ❌ Error! Python looks for a variable named Alice
```

---

### 4. **Booleans** (bool) - True or False

Booleans have only TWO possible values: `True` or `False`.

```python
is_student = True         # Boolean True
is_raining = False        # Boolean False
likes_pizza = True        # Most people like pizza!
```

**Important:** `True` and `False` start with capital letters!

```python
print(True)   # ✅ Correct
print(true)   # ❌ Error!
```

**Use booleans for:**
- Yes/No questions
- On/Off states
- Checking if something is true

---

## Checking Data Types

You can check what type a variable is using `type()`:

```python
print(type(14))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>
```

---

## Mixing Data Types

```python
# Different types together
student_name = "Alice"      # String
student_age = 14            # Integer
student_height = 5.6        # Float
is_senior = False           # Boolean

# Print them
print("Name:", student_name)
print("Age:", student_age)
print("Height:", student_height)
print("Senior Student:", is_senior)
```

---

## Common Mistakes

### ❌ Mistake 1: Forgetting Quotes for Strings
```python
name = Alice      # ❌ Error! Missing quotes
name = "Alice"    # ✅ Correct
```

### ❌ Mistake 2: Wrong Case for Booleans
```python
print(true)       # ❌ Error! Should be True
print(True)       # ✅ Correct
```

### ❌ Mistake 3: Mixing Numbers and Strings
```python
age = "14"        # This is a STRING, not a number!
age = 14          # This is a NUMBER
```

---

## Exercise

Create a Python file called `lesson2.py` with these variables:

1. Your name (string)
2. Your age (integer)
3. Your height (float)
4. Whether you like coding (boolean)
5. Your favorite food (string)
6. Number of siblings (integer)

Then print each one with its data type.

Example:
```python
my_name = "Your Name"
my_age = 14
my_height = 5.7
like_coding = True
favorite_food = "Pizza"
siblings = 2

print(my_name, type(my_name))
print(my_age, type(my_age))
print(my_height, type(my_height))
print(like_coding, type(like_coding))
print(favorite_food, type(favorite_food))
print(siblings, type(siblings))
```

---

## Key Points

✍️ **Integer (int)**: Whole numbers (14, -5, 0, 100)
✍️ **Float (float)**: Decimal numbers (3.14, 5.6, 9.99)
✍️ **String (str)**: Text in quotes ("Alice", 'hello')
✍️ **Boolean (bool)**: True or False
✍️ Use `type()` to check what type a variable is
✍️ Strings MUST have quotes!
✍️ Booleans use capital letters (True, False)

---

## Next: Lesson 3 - Basic Operators

Learn how to do math and combine data with operators (+, -, *, /, %, **)
