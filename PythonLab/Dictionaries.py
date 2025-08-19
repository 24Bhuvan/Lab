# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing items
print("Name:", my_dict["name"]) 
print("Age:", my_dict.get("age"))  # Using get() method

# Changing items
my_dict["city"] = "Los Angeles"
print("Updated city:", my_dict["city"])

# Adding items
my_dict["country"] = "USA"
print("Dictionary after adding country:", my_dict)

# Removing items
del my_dict["age"] 
print("Dictionary after deleting age:", my_dict)
my_dict.pop("city") 
print("Dictionary after popping city:", my_dict)

# Looping through items
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Copying dictionaries
dict1 = my_dict.copy()  # Shallow copy
dict2 = my_dict  # Reference to the same dictionary

dict1["name"] = "Bob" 
print("dict1:", dict1)
print("my_dict:", my_dict)  # Original dictionary remains unchanged in shallow copy

# Nested dictionaries
nested_dict = {
    "person1": {"name": "John", "age": 25},
    "person2": {"name": "Jane", "age": 30}
}

print("Nested dictionary:", nested_dict)
print("Person1's name:", nested_dict["person1"]["name"])