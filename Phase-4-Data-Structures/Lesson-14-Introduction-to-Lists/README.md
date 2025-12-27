# Lesson 14: Introduction to Lists

## Learning Objectives

- Understand what lists are and how to create them
- Learn list indexing and slicing
- Master common list methods
- Understand list iteration
- Work with mutable sequences

## Key Concepts

### What are Lists?
Lists are ordered, mutable collections of items in Python. They can contain elements of different data types.

### Creating Lists
```python
# Empty list
empty_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]
```

### List Indexing
```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])   # apple
print(fruits[-1])  # orange (last element)
```

### List Slicing
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:3])     # [2, 3]
print(numbers[:2])      # [1, 2]
print(numbers[2:])      # [3, 4, 5]
```

### Common List Methods
```python
fruits = ["apple", "banana"]
fruits.append("orange")      # Add single element
fruits.extend(["grape"])     # Add multiple elements
fruits.insert(1, "mango")    # Insert at position
fruits.remove("banana")      # Remove by value
fruits.pop(0)                # Remove by index
fruits.sort()                # Sort the list
fruits.reverse()             # Reverse the list
fruits.copy()                # Create a shallow copy
```

## Resources

- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- Practice the concepts with the examples.py and exercises.py files
