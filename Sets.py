# Creating a set
my_set = {1, 2, 3, 3, 4}  # Duplicates are automatically removed
print("Set:", my_set)  # Output: {1, 2, 3, 4}

# Accessing items (indirectly)
print("Accessing items:")
for item in my_set:
    print(item)

# Adding items
my_set.add(5)
print("Set after adding 5:", my_set)

# Removing items
my_set.remove(3)  # Raises KeyError if item not found
print("Set after removing 3:", my_set)
my_set.discard(6)  # Does not raise error if item not found
print("Set after discarding 6:", my_set)
my_set.pop()  # Removes and returns an arbitrary element
print("Set after popping:", my_set)

# Joining sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Combine elements from both sets
print("Union of sets:", union_set) 
intersection_set = set1.intersection(set2)  # Find common elements
print("Intersection of sets:", intersection_set)

# Set methods
# Difference: Elements in set1 but not in set2
difference_set = set1.difference(set2)
print("Difference of set1 from set2:", difference_set)

# Symmetric difference: Elements in either set1 or set2, but not in both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of sets:", symmetric_difference_set)

# Checking if a set is a subset of another
is_subset = set1.issubset(set2) 
print("Is set1 a subset of set2?", is_subset)

# Checking if a set is a superset of another
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)

# Clearing the set
my_set.clear()
print("Cleared set:", my_set)