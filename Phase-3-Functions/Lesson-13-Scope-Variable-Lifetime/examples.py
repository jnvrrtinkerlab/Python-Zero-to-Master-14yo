"""
Lesson 13: Scope and Variable Lifetime - Examples
"""

# Example 1: Local Scope
def func1():
    x = 10  # Local variable
    print(f"Inside func1: x = {x}")

func1()
# print(x)  # Would cause NameError - x is not defined in global scope


# Example 2: Global Scope
y = 20  # Global variable

def func2():
    print(f"Inside func2: y = {y}")

func2()
print(f"Global scope: y = {y}")


# Example 3: Modifying Global Variables with 'global' keyword
count = 0

def increment():
    global count
    count += 1
    print(f"Count: {count}")

increment()
increment()
print(f"Final count: {count}")


# Example 4: Local Variable Shadows Global
name = "Global"

def test_shadow():
    name = "Local"  # Shadows global variable
    print(f"Inside function: {name}")

test_shadow()
print(f"Outside function: {name}")


# Example 5: Nested Functions and Enclosing Scope
def outer():
    x = 5  # Enclosing scope
    
    def inner():
        nonlocal x  # Access enclosing scope variable
        x += 1
        print(f"Inner: x = {x}")
    
    inner()
    print(f"Outer: x = {x}")

outer()


# Example 6: Variable Lifetime
def create_variables():
    temp = "I exist only in this function"
    print(temp)
    # When function ends, 'temp' is destroyed

create_variables()
# temp is no longer accessible


# Example 7: Scope with Loops
for i in range(3):
    pass
print(f"After loop, i = {i}")  # i is still accessible in Python 3


# Example 8: Default Mutable Arguments (Scope Issue)
def append_to(element, to=[]):
    to.append(element)
    return to

list1 = append_to(1)
list2 = append_to(2)
print(f"list1: {list1}, list2: {list2}")  # Both share same list!


# Example 9: LEGB Rule Demonstration
x = "global"

def outer_func():
    x = "enclosing"
    
    def inner_func():
        x = "local"
        print(f"Local: {x}")
    
    inner_func()
    print(f"Enclosing: {x}")

outer_func()
print(f"Global: {x}")


# Example 10: Namespace Access with vars() and dir()
def show_scope():
    local_var = 42
    print(f"Local variables: {list(vars().keys())}")

show_scope()
print(f"Global variables (sample): {[k for k in dir() if not k.startswith('_')][:5]}")


print("\n=== Lesson 13 Complete ===")
