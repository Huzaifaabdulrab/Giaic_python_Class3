# CONTROL FLOW

# Checking grades using if-elif-else statements
marks = 85
if marks >= 90:
    print("Your grade: A+")
elif marks >= 80:
    print("Your grade: A")  # ✅ This condition is true
elif marks >= 70:
    print("Your grade: B")
else:
    print("Your grade: Fail")

# Iterating over a list using a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

# Using break to stop a loop
for num in range(10):
    if num == 5:
        break  # ✅ Loop stops here
    print(num)

# Output:
# 0
# 1
# 2
# 3
# 4

# Using continue to skip an iteration
for num in range(5):
    if num == 2:
        continue  # ✅ Skips this iteration
    print(num)

# Output:
# 0
# 1
# 3
# 4

# Using a for loop with range
for num in range(1, 11):
    print(num)  # 1 2 3 4 5 6 7 8 9 10

# Using a while loop
count = 1
while count <= 5:
    print(count)
    count += 1  # ✅ Necessary to avoid an infinite loop

# Output:
# 1
# 2
# 3
# 4
# 5

# LIST OPERATIONS

# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing an element by index
print(fruits[1])  # Output: banana

# Adding an element to the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Inserting an element at a specific index
fruits.insert(1, "grape")
print(fruits)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']

# Removing an element
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange']

# Modifying a list
numbers = [10, 20, 30, 40]
numbers[2] = 35  # Changing an element
print(numbers)  # Output: [10, 20, 35, 40]

# Reversing the list
numbers.reverse()
print(numbers)  # Output: [40, 35, 20, 10]

# Sorting the list
numbers.sort()
print(numbers)  # Output: [10, 20, 35, 40]

# TUPLE OPERATIONS

# Creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')

# Accessing an element in a tuple
print(fruits[1])  # Output: banana

# Tuples are immutable (cannot be modified)
# fruits[1] = "grape"  # ❌ This will raise an error

# DICTIONARY OPERATIONS

# Creating a dictionary
person = {
    "name": "Ali",
    "age": 25,
    "city": "Karachi"
}
print(person)  # Output: {'name': 'Ali', 'age': 25, 'city': 'Karachi'}

# Accessing a value by key
print(person["name"])  # Output: Ali

# Adding a new key-value pair
person["job"] = "Engineer"
print(person)  # Output: {'name': 'Ali', 'age': 25, 'city': 'Karachi', 'job': 'Engineer'}

# Updating a value
person["age"] = 26
print(person)  # Output: {'name': 'Ali', 'age': 26, 'city': 'Karachi', 'job': 'Engineer'}

# Removing a key-value pair
del person["city"]
print(person)  # Output: {'name': 'Ali', 'age': 26, 'job': 'Engineer'}

# SET OPERATIONS

# Creating a set
my_set = {1, 2, 3}
my_set.add(4)  # ✅ Allowed
print(my_set)  # Output: {1, 2, 3, 4}

# FROZENSET OPERATIONS

# Creating a frozenset
my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4)  # ❌ Not allowed, will raise an error