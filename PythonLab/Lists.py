# LISTS
# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements 

# Creating a list
# List of integers
numbers = [1, 2, 3, 4, 5] 
print("List of integers:", numbers)

# List of strings
fruits = ["apple", "banana", "cherry"]
print("List of fruits:", fruits)

# List of mixed data types
mixed_list = [10, "hello", True, 3.14]
print("List of mixed data types:", mixed_list)

# Empty list
empty_list = []
print("Empty list:", empty_list)


# Accessing List Elements

# Accessing elements by index (zero-based indexing)
first_fruit = fruits[0]  # Accesses the first element ("apple")
print("First fruit:", first_fruit)

last_number = numbers[-1]  # Accesses the last element (5)
print("Last number:", last_number)


# Changing List Elements

# Modifying an element
fruits[1] = "orange"  # Replace "banana" with "orange"
print("Updated fruits list:", fruits)


# Adding Elements to a List

# Using append() to add an element at the end
numbers.append(6) 
print("Numbers list after appending:", numbers)

# Using insert() to add an element at a specific index
fruits.insert(1, "grape")  # Insert "grape" at index 1
print("Fruits list after inserting:", fruits)


# Removing Elements from a List

# Using remove() to remove the first occurrence of a specific value
fruits.remove("orange")
print("Fruits list after removing 'orange':", fruits)

# Using pop() to remove an element at a specific index
removed_number = numbers.pop(2)  # Remove the element at index 2
print("Removed number:", removed_number)
print("Numbers list after popping:", numbers)


# Loops in Lists

# Using a for loop to iterate over elements
for fruit in fruits:
    print(fruit)

# Using a for loop with range() to iterate over indices
for i in range(len(numbers)):
    print(f"Number at index {i}: {numbers[i]}")