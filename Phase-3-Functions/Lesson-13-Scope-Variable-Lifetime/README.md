# Lesson 13: Scope and Variable Lifetime

## Learning Objectives
- Understand local and global scope
- Master variable lifetime and accessibility
- Learn about nested scopes
- Avoid scope-related bugs
- Use scope effectively in larger programs

## What is Scope?

Scope determines where a variable can be accessed in your code. Python has several scope levels:

### Scope Levels
1. **Local Scope**: Variables inside a function
2. **Enclosing Scope**: Variables in outer functions (nested functions)
3. **Global Scope**: Variables at module level
4. **Built-in Scope**: Python's built-in functions and variables

## Variable Lifetime

Lifetime is the duration a variable exists in memory:
- Created when declared
- Accessible within its scope
- Destroyed when scope ends

## Key Concepts

- **Local Variables**: Exist only in function
- **Global Variables**: Exist throughout program
- **Namespace**: Dictionary of variable names and values
- **LEGB Rule**: Local, Enclosing, Global, Built-in

## Common Issues

- Accessing variables outside their scope
- Modifying global variables accidentally
- Name shadowing (same name in different scopes)
- UnboundLocalError

## Best Practices

- Keep variables local when possible
- Minimize global variable usage
- Use meaningful names
- Document variable purposes
