# TUPLES
# Creating a tuple
my_tuple = ("apple", "banana", "cherry", "orange")

# Accessing elements
print("First fruit:", my_tuple[0])  # Accessing the first element
print("Last fruit:", my_tuple[-1])  # Accessing the last element
print("Fruits from index 1 to 2:", my_tuple[1:3])  # Slicing

# Updating tuples (immutability - creating a new tuple)
new_tuple = my_tuple + ("grape",)  # Adding an element
print("New tuple:", new_tuple)

# Unpacking tuples
fruit1, fruit2, fruit3, fruit4 = my_tuple
print("Unpacked fruits:", fruit1, fruit2, fruit3, fruit4)

# Looping through a tuple
for fruit in my_tuple:
    print(fruit)

# Joining tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
joined_tuple = tuple1 + tuple2
print("Joined tuple:", joined_tuple)