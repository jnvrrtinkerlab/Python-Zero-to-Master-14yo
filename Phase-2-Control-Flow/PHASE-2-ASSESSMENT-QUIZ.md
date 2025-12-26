# Phase 2 Assessment Quiz

## Part 1: Multiple Choice (1 point each)

**Q1:** What does this code output?
```python
for i in range(3):
    print(i)
```
A) 1, 2, 3  
B) 0, 1, 2  
C) 0, 1, 2, 3  
D) 1, 2  

**Answer: B** (range(3) is 0 to 2)

---

**Q2:** Which statement will exit a while loop?
A) `continue`  
B) `break`  
C) `exit()`  
D) `stop()`  

**Answer: B** (break exits, continue skips)

---

**Q3:** What is the output?
```python
if 5 > 3:
    print("Yes")
else:
    print("No")
```
A) Yes  
B) No  
C) YesNo  
D) Error  

**Answer: A** (5 > 3 is True)

---

**Q4:** How many times does this loop run?
```python
for i in range(1, 5):
    print(i)
```
A) 4 times  
B) 5 times  
C) 3 times  
D) 6 times  

**Answer: A** (range(1, 5) = 1,2,3,4)

---

**Q5:** What's wrong with this code?
```python
while count < 5:
    print(count)
# Missing:
```
A) Missing break  
B) Missing count increment  
C) Missing input()  
D) Missing if statement  

**Answer: B** (Loop never increments, infinite loop)

---

## Part 2: Code Output (2 points each)

**Q6:** What's the output?
```python
for num in range(2, 6, 2):
    print(num)
```
Output: `2 4`

---

**Q7:** What's the output?
```python
age = 15
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```
Output: `Teen`

---

**Q8:** What's the output?
```python
count = 0
while count < 3:
    print(count)
    count += 1
```
Output:
```
0
1
2
```

---

**Q9:** What's the output?
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```
Output: `0 1 3 4` (skips 2)

---

**Q10:** What's the output?
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```
Output: `0 1 2` (exits when i=3)

---

## Part 3: Fix the Code (3 points each)

**Q11:** Fix this infinite loop:
```python
while True:
    num = int(input("Enter 0 to exit: "))
    # Add code here
```

**Answer:**
```python
while True:
    num = int(input("Enter 0 to exit: "))
    if num == 0:
        break  # Exit when 0 is entered
    print(f"You entered: {num}")
```

---

**Q12:** Fix the indentation error:
```python
age = int(input("Age: "))
if age >= 18:
print("Adult")
```

**Answer:**
```python
age = int(input("Age: "))
if age >= 18:
    print("Adult")  # Proper indentation
```

---

**Q13:** Fix the off-by-one error:
```python
# Print 1 to 5
for i in range(5):  # Wrong!
    print(i)
```

**Answer:**
```python
for i in range(1, 6):  # Correct (1 to 5)
    print(i)
```

---

## Part 4: Coding Problems (5 points each)

**Q14:** Write a program that asks for a number and prints if it's even or odd.

**Sample Answer:**
```python
num = int(input("Enter number: "))
if num % 2 == 0:
    print(f"{num} is EVEN")
else:
    print(f"{num} is ODD")
```

---

**Q15:** Write a program that counts from 1 to 10 but skips multiples of 3.

**Sample Answer:**
```python
for i in range(1, 11):
    if i % 3 == 0:
        continue  # Skip multiples of 3
    print(i)
# Output: 1 2 4 5 7 8 10
```

---

**Q16:** Write a login program with max 3 attempts.

**Sample Answer:**
```python
password = "python123"
attempts = 0

while attempts < 3:
    user_pass = input("Password: ")
    if user_pass == password:
        print("Access granted!")
        break
    attempts += 1
    print(f"Wrong! Attempts left: {3 - attempts}")

if attempts == 3:
    print("Account locked!")
```

---

## Scoring

- Part 1: 5 questions × 1 point = 5 points
- Part 2: 5 questions × 2 points = 10 points
- Part 3: 3 questions × 3 points = 9 points
- Part 4: 3 questions × 5 points = 15 points
- **Total: 39 points**

### Grade Scale
- 35-39 points: A (90-100%)
- 31-34 points: B (80-89%)
- 27-30 points: C (70-79%)
- 23-26 points: D (60-69%)
- Below 23: F (below 60%)

---

## Answer Key Available
Ask your instructor for the complete answer key.

*Last Updated: December 2024*
