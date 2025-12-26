# Lesson 10: Loop Control (Break & Continue)

## Objectives
- Exit loops with `break`
- Skip iterations with `continue`
- Control loop flow

## Concepts
1. **Break** - Exit loop immediately
2. **Continue** - Skip to next iteration
3. **Usage** - When and how to use each

## Code Examples

### Break
```python
while True:
    num = int(input("Enter 0 to exit: "))
    if num == 0:
        break
    print(num)
```

### Continue
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # 1,2,4,5
```

### Search
```python
for name in ["Ali", "Sara", "Khan"]:
    if name == "Khan":
        print("Found!")
        break
```

### Filter
```python
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)  # Odd only
```

## Exercises
1. Find first match and break
2. Skip multiples
3. Password retry
4. Menu system
5. Data filter

## Phase 2 Complete
All 5 lessons cover control flow concepts!

---

*Last Updated: December 2024*
