# Phase 2: Control Flow in Python

**Master conditional statements, loops, and logical reasoning - The foundation of dynamic programming**

---

## 📚 Phase Overview

**Duration:** 2 weeks | **Difficulty Level:** Beginner to Intermediate  
**Prerequisites:** Phase 1 (Variables, Data Types, Operations) completed

Phase 2 focuses on **control flow structures** that enable programs to make decisions and repeat actions. You'll learn how to write smarter code that responds to different situations and automates repetitive tasks.

### Learning Outcomes
By the end of this phase, students will:
- ✅ Write conditional statements using `if`, `elif`, and `else`
- ✅ Create and control loops with `while` and `for`
- ✅ Use logical operators (`and`, `or`, `not`) effectively
- ✅ Break and continue loop execution
- ✅ Build nested conditions and complex logic
- ✅ Apply control flow in real-world problems

---

## 🎯 Lesson Structure (Sequential Order)

### **Lesson 6: Introduction to Conditional Statements**
📂 **Folder:** `Lesson-6-If-Else-Basics`

**Topics Covered:**
- What are conditional statements?
- The `if` statement structure and syntax
- Boolean values (`True`, `False`)
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Simple `if` block execution
- Indentation rules and best practices

**Learning Goals:**
- Understand how programs make decisions
- Write basic `if` statements
- Use comparison operators correctly
- Debug indentation errors

**Key Concepts:**
```python
# Basic if statement
age = 15
if age >= 13:
    print("You can watch this content")
```

**Activities:**
- Compare numbers and strings
- Create programs that respond to user input
- Analyze boolean expressions
- Write conditional blocks

**Practice Challenges:**
- Check if a number is positive
- Determine if a student passed or failed
- Age verification system

---

### **Lesson 7: Expanding Conditionals (elif and else)**
📂 **Folder:** `Lesson-7-Elif-Else-Advanced`

**Topics Covered:**
- The `else` block for alternative actions
- The `elif` (else if) for multiple conditions
- Chaining multiple `elif` blocks
- Nested `if` statements
- Best practices for condition ordering
- Common pitfalls and solutions

**Learning Goals:**
- Handle multiple possible outcomes
- Write efficient conditional chains
- Nest conditions appropriately
- Improve code readability

**Key Concepts:**
```python
# Multiple conditions
score = 78
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print(f"Your grade: {grade}")
```

**Activities:**
- Grade calculator
- Traffic light system simulator
- Weather-based recommendations
- Decision trees

**Practice Challenges:**
- Letter grade assignment (A, B, C, D, F)
- BMI (Body Mass Index) calculator
- Movie rating classifier

---

### **Lesson 8: Logical Operators and Complex Conditions**
📂 **Folder:** `Lesson-8-Logical-Operators`

**Topics Covered:**
- The `and` operator (both conditions true)
- The `or` operator (at least one true)
- The `not` operator (negation)
- Truth tables and logical logic
- Operator precedence in boolean expressions
- De Morgan's Laws
- Combining multiple conditions efficiently

**Learning Goals:**
- Build complex boolean expressions
- Understand truth tables
- Write concise logical conditions
- Debug complex conditionals

**Key Concepts:**
```python
# Logical operators
age = 16
has_license = True

if age >= 16 and has_license:
    print("You can drive!")

if age < 13 or grade < 6:
    print("Parental permission required")

if not blocked:
    print("Access granted")
```

**Activities:**
- Permission systems (age AND license)
- Range checking (x > 10 and x < 20)
- OR conditions (multiple valid options)
- Negation logic

**Practice Challenges:**
- Login validation (username AND password)
- Temperature alert system (too hot OR too cold)
- Age-appropriate content filter

---

### **Lesson 9: Introduction to Loops (while)**
📂 **Folder:** `Lesson-9-While-Loops`

**Topics Covered:**
- What are loops and why we need them
- The `while` loop structure
- Loop conditions and termination
- Counter-controlled loops
- Accumulator patterns
- Infinite loops and how to avoid them
- Loop best practices

**Learning Goals:**
- Understand when to use loops
- Write working `while` loops
- Control loop iterations
- Avoid common loop errors
- Use accumulators effectively

**Key Concepts:**
```python
# While loop - repeat until condition is false
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Accumulator pattern
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Sum: {total}")
```

**Activities:**
- Countdown timer
- Sum calculator (sum first N numbers)
- User input validation loop
- Number guessing game

**Practice Challenges:**
- Calculate factorial using while loop
- Calculate average of user-entered numbers
- Password validation system

---

### **Lesson 10: Advanced Loops (for) and Loop Control**
📂 **Folder:** `Lesson-10-For-Loops-Advanced`

**Topics Covered:**
- The `for` loop and `range()` function
- Iterating with `for` loops
- `break` statement (exit loop early)
- `continue` statement (skip to next iteration)
- Nested loops
- `else` block with loops
- Choosing between `while` and `for`
- Loop optimization

**Learning Goals:**
- Use `for` loops efficiently
- Control loop flow with `break` and `continue`
- Work with nested loops
- Choose appropriate loop types
- Optimize loop performance

**Key Concepts:**
```python
# For loop with range
for i in range(5):
    print(f"Iteration {i}")

# Break statement
for num in range(10):
    if num == 5:
        break  # Exit loop
    print(num)

# Continue statement
for num in range(10):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

**Activities:**
- Multiplication table generator
- Pattern printing (triangles, squares)
- Search and stop (find item in list)
- Nested loop puzzles
- Skipping numbers (even/odd filtering)

**Practice Challenges:**
- Create a 5x5 grid pattern
- Find and stop at first prime number
- Sum only odd numbers from 1 to 50
- Create a simple menu system with loop

---

## 🔗 Learning Path

```
Phase 2: Control Flow
├── Lesson 6: If-Else Basics
│   └── Foundation: Single decision making
├── Lesson 7: Elif-Else Advanced
│   └── Building: Multiple outcomes
├── Lesson 8: Logical Operators
│   └── Strengthening: Complex conditions
├── Lesson 9: While Loops
│   └── Automating: Condition-based repetition
└── Lesson 10: For Loops & Loop Control
    └── Mastering: Complete loop control
```

---

## 📁 Directory Structure

```
Phase-2-Control-Flow/
├── Lesson-6-If-Else-Basics/
│   ├── README.md
│   ├── Notes.md
│   ├── examples.py
│   └── exercises.py
├── Lesson-7-Elif-Else-Advanced/
│   ├── README.md
│   ├── Notes.md
│   ├── examples.py
│   └── exercises.py
├── Lesson-8-Logical-Operators/
│   ├── README.md
│   ├── Notes.md
│   ├── examples.py
│   └── exercises.py
├── Lesson-9-While-Loops/
│   ├── README.md
│   ├── Notes.md
│   ├── examples.py
│   └── exercises.py
├── Lesson-10-For-Loops-Advanced/
│   ├── README.md
│   ├── Notes.md
│   ├── examples.py
│   └── exercises.py
├── TEACHER_RESOURCES/
│   ├── INSTRUCTOR_GUIDE.md
│   ├── DEBUGGING_AND_ERRORS.md
│   └── ADVANCED_CHALLENGES.md
├── CAPSTONE_PROJECT/
│   ├── PROJECT_BRIEF.md
│   └── starter_code.py
├── QUIZ_AND_ASSESSMENT/
│   ├── Quiz.md
│   └── Solutions.md
└── README.md
```

---

## 🎓 Support Resources

### For Students
- **Stuck on a concept?** → Review the lesson README
- **Error in your code?** → Check [DEBUGGING_AND_ERRORS.md](./TEACHER_RESOURCES/DEBUGGING_AND_ERRORS.md)
- **Want more practice?** → Try [ADVANCED_CHALLENGES.md](./TEACHER_RESOURCES/ADVANCED_CHALLENGES.md)
- **Ready for a big project?** → Start the [CAPSTONE_PROJECT](./CAPSTONE_PROJECT/)

### For Teachers
- **Teaching guide** → [INSTRUCTOR_GUIDE.md](./TEACHER_RESOURCES/INSTRUCTOR_GUIDE.md)
- **Common mistakes** → [DEBUGGING_AND_ERRORS.md](./TEACHER_RESOURCES/DEBUGGING_AND_ERRORS.md)
- **Assessment tools** → [QUIZ_AND_ASSESSMENT](./QUIZ_AND_ASSESSMENT/)
- **Extended learning** → [ADVANCED_CHALLENGES.md](./TEACHER_RESOURCES/ADVANCED_CHALLENGES.md)

---

## 📊 Learning Progression

| Lesson | Topic | Difficulty | Time | Focus |
|--------|-------|----------|------|-------|
| 6 | If-Else Basics | ⭐ | 2-3h | Single decisions |
| 7 | Elif-Else Advanced | ⭐⭐ | 3-4h | Multiple outcomes |
| 8 | Logical Operators | ⭐⭐ | 3-4h | Complex logic |
| 9 | While Loops | ⭐⭐ | 3-4h | Condition-based repetition |
| 10 | For Loops & Control | ⭐⭐⭐ | 4-5h | Complete loop mastery |

**Total Phase Duration:** 15-20 hours

---

## 🚀 Getting Started

1. **Start with Lesson 6:** Open `Lesson-6-If-Else-Basics/README.md`
2. **Read the notes:** Understand the concepts in `Notes.md`
3. **Study examples:** Run `examples.py` and modify them
4. **Practice exercises:** Complete `exercises.py`
5. **Move to next lesson:** Progress sequentially

---

## ✅ Completion Checklist

- [ ] Lesson 6: If-Else Basics completed
- [ ] Lesson 7: Elif-Else Advanced completed
- [ ] Lesson 8: Logical Operators mastered
- [ ] Lesson 9: While Loops working
- [ ] Lesson 10: For Loops & Loop Control mastered
- [ ] All exercises solved
- [ ] Capstone Project completed
- [ ] Quiz passed (70%+)

---

## 🎯 Real-World Applications

Control Flow is used everywhere in software:
- **Games:** Player decisions and game loops
- **Banking:** Transaction validation and processing
- **Social Media:** Checking permissions and filtering content
- **Automation:** Repeating tasks until done
- **Data Processing:** Filtering and transforming data
- **Websites:** User authentication and navigation

---

## 📈 Next Phase

After completing Phase 2, you'll be ready for **Phase 3: Data Structures** where you'll learn:
- Lists and list operations
- Dictionaries and key-value pairs
- Tuples and their uses
- Sets and unique values

---

## 📝 Notes

- **Last Updated:** January 2025
- **Status:** ✅ Complete & Ready to Use
- **Version:** 2.0
- **Maintained by:** Jawahar Navodaya Vidyalaya Robotics Lab

---

**Happy Learning! Control the flow of your code! 🎉**
