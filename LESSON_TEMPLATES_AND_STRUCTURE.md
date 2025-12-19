LESSON_TEMPLATES_AND_STRUCTURE.md# Complete Lesson Templates & Course Structure
## All 40 Lessons Outlined with Key Concepts

---

## PHASE 1: PYTHON BASICS (Lessons 1-5)

### Lesson 1: Variables & Print Statements ✅
- Creating variables
- Using print() function
- Naming conventions
- First program

### Lesson 2: Data Types (Numbers, Strings, Booleans) ✅
- Integers (int): whole numbers
- Floats (float): decimal numbers
- Strings (str): text data
- Booleans (bool): True/False
- type() function

### Lesson 3: Basic Operators ✅
- Arithmetic: +, -, *, /, //, %, **
- Comparison: ==, !=, <, >, <=, >=
- Assignment: =, +=, -=, *=, /=
- Order of operations (PEMDAS)

### Lesson 4: User Input
**Topics:**
- input() function
- Converting input to numbers (int(), float())
- Getting user information
- Simple interactive programs

**Key Concepts:**
```python
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hello {name}, you are {age} years old")
```

**Exercise:** Create a program that asks for name, age, and favorite subject, then displays them.

### Lesson 5: Simple Project - Calculate Circle Area
**Project Goals:**
- Use variables to store values
- Get user input
- Perform calculations
- Display results

**Project Outline:**
1. Get radius from user
2. Calculate area using formula: A = π * r²
3. Display result

**Code Template:**
```python
import math
radius = float(input("Enter circle radius: "))
area = math.pi * (radius ** 2)
print(f"Area of circle: {area:.2f}")
```

---

## PHASE 2: CONTROL FLOW (Lessons 6-10)

### Lesson 6: If/Else Statements
**Topics:**
- Boolean expressions
- if statement
- if/else structure
- Indentation importance

**Key Concepts:**
```python
age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a teenager")
```

### Lesson 7: Advanced Conditions (elif, and, or)
**Topics:**
- elif (else if) statements
- Logical operators: and, or, not
- Multiple conditions
- Complex decision making

**Key Concepts:**
```python
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

### Lesson 8: While Loops
**Topics:**
- Repeating code with while
- Loop conditions
- Infinite loops (and how to avoid them)
- Counter variables

**Key Concepts:**
```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

### Lesson 9: For Loops
**Topics:**
- range() function
- for loop syntax
- Iterating with for
- Loop variable

**Key Concepts:**
```python
for i in range(5):
    print(f"Number: {i}")

for animal in ["dog", "cat", "bird"]:
    print(animal)
```

### Lesson 10: Loop Control (Break & Continue)
**Topics:**
- break statement
- continue statement
- Skipping iterations
- Exiting loops early

**Key Concepts:**
```python
for i in range(10):
    if i == 5:
        break  # Exit loop
    if i == 2:
        continue  # Skip this iteration
    print(i)
```

---

## PHASE 3: FUNCTIONS (Lessons 11-15)

### Lesson 11: Introduction to Functions
- What are functions?
- def keyword
- Calling functions
- Organizing code

### Lesson 12: Parameters & Arguments
- Adding parameters
- Passing arguments
- Multiple parameters
- Default parameters

### Lesson 13: Return Values
- Return statement
- Getting results from functions
- Using returned values

### Lesson 14: Scope & Global Variables
- Local variables
- Global variables
- Variable scope
- Avoiding bugs with scope

### Lesson 15: Function Practice Project
- Calculator with functions
- Function organization
- Code reusability

---

## PHASE 4: DATA STRUCTURES (Lessons 16-20)

### Lesson 16: Lists & Indexing
- Creating lists
- Accessing elements
- Negative indexing
- Slicing

### Lesson 17: List Methods
- append(), insert(), remove()
- sort(), reverse()
- len(), index()
- List iteration

### Lesson 18: Dictionaries
- Key-value pairs
- Creating dictionaries
- Accessing values
- Adding/modifying entries

### Lesson 19: Tuples & Sets
- Immutable tuples
- Unique sets
- When to use each

### Lesson 20: Data Structure Project
- Student database with dictionaries
- Storing multiple students
- Searching and displaying data

---

## PHASE 5: FILE HANDLING (Lessons 21-25)

### Lesson 21: Reading Files
- open() function
- read() method
- File paths

### Lesson 22: Writing Files
- Writing to files
- Append mode
- Creating new files

### Lesson 23: Working with CSV Files
- CSV format
- Reading CSV data
- Writing to CSV

### Lesson 24: JSON Data
- JSON format
- json library
- Saving/loading JSON

### Lesson 25: File Handling Project
- Grade tracker application
- Save grades to file
- Load and display grades

---

## PHASE 6: OBJECT-ORIENTED PROGRAMMING (Lessons 26-30)

### Lesson 26: What are Classes & Objects?
- Classes as blueprints
- Objects as instances
- Real-world examples

### Lesson 27: Creating Your First Class
- class keyword
- __init__ method
- Creating instances

### Lesson 28: Methods & Attributes
- Instance variables
- Methods
- self keyword

### Lesson 29: Inheritance
- Parent classes
- Child classes
- super() function

### Lesson 30: OOP Project
- Create Student class
- Add methods
- Inheritance example

---

## PHASE 7: LIBRARIES & MODULES (Lessons 31-35)

### Lesson 31: Introduction to Libraries
- What are libraries?
- import statement
- Standard library overview

### Lesson 32: Working with Requests
- HTTP requests
- Getting data from APIs
- Parsing responses

### Lesson 33: Data Analysis with Pandas
- DataFrames
- Reading CSV/Excel
- Data manipulation

### Lesson 34: Visualization with Matplotlib
- Creating charts
- Line plots, bar graphs
- Customizing visualizations

### Lesson 35: Creating Modules
- Organizing code into modules
- Using your own modules
- Sharing code

---

## PHASE 8: FINAL PROJECTS (Lessons 36-40)

### Lesson 36: Todo List Application
- User menu system
- Add/remove/display tasks
- Save to file
- Full OOP design

### Lesson 37: Calculator Program
- Multi-operation calculator
- Error handling
- User interface
- Functions for each operation

### Lesson 38: Quiz Game
- Store questions in data structure
- Track score
- Display questions and answers
- End-game summary

### Lesson 39: Web Scraper
- requests library
- HTML parsing
- Extract information
- Save data

### Lesson 40: Personal Capstone Project
- Student chooses topic
- Combines all learned concepts
- Project presentation
- Code documentation

---

## How to Use This Template

Each lesson should include:
1. **Theory Section** - Explain concepts in simple terms
2. **Code Examples** - Show working code
3. **Common Mistakes** - What NOT to do
4. **Practical Exercise** - Hands-on practice
5. **Key Points** - Summary of takeaways

## Next Steps

1. Create individual README.md files for each lesson
2. Add example code files (.py) for each lesson
3. Include solutions for exercises
4. Add difficulty levels (Beginner/Intermediate/Advanced)
5. Include video tutorial links

---

## For Teachers/Mentors

- Encourage students to type code, not copy-paste
- Give time for experimentation
- Celebrate mistakes as learning opportunities
- Adjust pace based on student progress
- Have students explain code to you
- Create group projects for collaboration

---

**Status:** Framework complete. Individual lesson details being added. ✅
