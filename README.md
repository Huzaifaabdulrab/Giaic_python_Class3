# Python Control Flow, Loops, Lists, Tuples, Dictionaries, Sets, and Frozensets

## Control Flow

### If-Else Statements
Control flow determines the execution path of a program. In Python, `if`, `elif`, and `else` are used for decision-making.

```python
marks = 85

if marks >= 90:
    print("Your grade: A+")
elif marks >= 80:
    print("Your grade: A")  # ✅ This condition is true
elif marks >= 70:
    print("Your grade: B")
else:
    print("Your grade: Fail")
```

## Loops

### For Loop
Used to iterate over a sequence such as a list, tuple, or string.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

### Using `break` in Loops
Stops the loop when a specific condition is met.

```python
for num in range(10):
    if num == 5:
        break  # ✅ Loop stops here
    print(num)
```

**Output:**
```
0
1
2
3
4
```

### Using `continue` in Loops
Skips the current iteration and moves to the next one.

```python
for num in range(5):
    if num == 2:
        continue  # ✅ Skips iteration when num is 2
    print(num)
```

**Output:**
```
0
1
3
4
```

### While Loop
Runs as long as the condition remains `True`.

```python
count = 1
while count <= 5:
    print(count)
    count += 1  # ✅ Necessary to prevent infinite loop
```

**Output:**
```
1
2
3
4
5
```

---

## Lists

Lists are mutable (changeable) collections of elements.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # ['apple', 'banana', 'cherry']

print(fruits[1])  # Access element: 'banana'

fruits.append("orange")  # Add element to list
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "grape")  # Insert at specific index
print(fruits)  # ['apple', 'grape', 'banana', 'cherry', 'orange']

fruits.remove("banana")  # Remove an element
print(fruits)  # ['apple', 'grape', 'cherry', 'orange']
```

### List Modification

```python
numbers = [10, 20, 30, 40]
numbers[2] = 35  # Modify an element
print(numbers)  # [10, 20, 35, 40]

numbers.reverse()  # Reverse list
print(numbers)  # [40, 35, 20, 10]

numbers.sort()  # Sort list
print(numbers)  # [10, 20, 35, 40]
```

---

## Tuples

Tuples are immutable (cannot be changed after creation).

```python
fruits = ("apple", "banana", "cherry")
print(fruits)  # ('apple', 'banana', 'cherry')

print(fruits[1])  # Access element: 'banana'

# Tuples cannot be modified
# fruits[1] = "grape"  # ❌ This will raise an error
```

---

## Dictionaries

Dictionaries store key-value pairs.

```python
person = {
    "name": "Ali",
    "age": 25,
    "city": "Karachi"
}
print(person)  # {'name': 'Ali', 'age': 25, 'city': 'Karachi'}

print(person["name"])  # Access value: 'Ali'

person["job"] = "Engineer"  # Add new key-value pair
print(person)  # {'name': 'Ali', 'age': 25, 'city': 'Karachi', 'job': 'Engineer'}

person["age"] = 26  # Update value
print(person)  # {'name': 'Ali', 'age': 26, 'city': 'Karachi', 'job': 'Engineer'}

del person["city"]  # Remove key-value pair
print(person)  # {'name': 'Ali', 'age': 26, 'job': 'Engineer'}
```

---

## Sets

Sets are unordered collections of unique elements.

```python
my_set = {1, 2, 3}
my_set.add(4)  # ✅ Allowed
print(my_set)  # Output: {1, 2, 3, 4}
```

---

## Frozensets

A `frozenset` is an immutable version of a set, meaning you cannot modify it after creation.

```python
my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4)  # ❌ This will raise an error
```

---

## Summary

- **Control Flow:** Uses `if-elif-else` for decision-making.
- **Loops:** `for` and `while` loops iterate over sequences or run while conditions are true.
- **Lists:** Mutable, ordered collections.
- **Tuples:** Immutable, ordered collections.
- **Dictionaries:** Key-value pairs for fast lookups.
- **Sets:** Unordered collections with unique elements.
- **Frozensets:** Immutable sets that cannot be modified.

This repository contains simple examples to understand these concepts in Python. 🚀

