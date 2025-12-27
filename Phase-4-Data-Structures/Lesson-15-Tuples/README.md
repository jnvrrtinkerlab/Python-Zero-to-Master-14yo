# Lesson 15: Tuples

## Learning Objectives

- Understand what tuples are and how they differ from lists
- Learn tuple indexing and slicing
- Master tuple methods
- Understand when to use tuples vs lists
- Work with tuple unpacking

## Key Concepts

### What are Tuples?
Tuples are ordered, immutable collections of items in Python. Once created, they cannot be modified.

### Creating Tuples
```python
# Empty tuple
empty_tuple = ()

# Tuple with elements
colors = ("red", "green", "blue")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Single element tuple (needs comma)
single = (42,)

# Tuple without parentheses
coordinates = 10, 20
```

### Tuple Indexing
```python
fruits = ("apple", "banana", "orange")
print(fruits[0])   # apple
print(fruits[-1])  # orange (last element)
```

### Tuple Slicing
```python
numbers = (1, 2, 3, 4, 5)
print(numbers[1:3])     # (2, 3)
print(numbers[:2])      # (1, 2)
print(numbers[2:])      # (3, 4, 5)
```

### Tuple Methods
```python
values = (1, 2, 2, 3, 2)
values.count(2)         # Count occurrences (returns 3)
values.index(3)         # Find index (returns 3)
```

### Tuple Unpacking
```python
point = (10, 20)
x, y = point
print(x, y)  # 10 20

# Multiple assignment
a, b, c = (1, 2, 3)
print(a, b, c)  # 1 2 3
```

### Why Tuples?
- Immutable (cannot be changed after creation)
- Can be used as dictionary keys
- Faster than lists for iteration
- Safer when data shouldn't be modified

## Resources

- [Python Tuples Documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- Practice the concepts with the examples.py and exercises.py files
