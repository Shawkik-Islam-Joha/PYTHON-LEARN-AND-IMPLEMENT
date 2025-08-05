numbers = {1, 2, 3, 4}         # Set with integers
fruits = {"apple", "banana", "apple"}  # Duplicate "apple" is removed

print(fruits)           # prints {'banana', 'apple'}

numbers.add(5)              # Add a new element
numbers.remove(3)           # Remove an element

a = {1, 2, 3}
b = {3, 4, 5}

print("Checking 2 in a set:",2 in a)                    # True
print("Checking 5 not in set a:",5 not in a)            # True

print(a | b)     # Union → {1, 2, 3, 4, 5}
print(a & b)     # Intersection → {3}
print(a - b)     # Difference → {1, 2}
print(a ^ b)     # Symmetric difference → {1, 2, 4, 5} , means all elements that are in either a or b, but not in both.

x = {1, 2, 3, 3, 4}
print(len(x))    # length will be 4 as duplicate 3 is removed

my_list = [1, 2, 2, 3, 4, 4]
unique = set(my_list)        # Removes duplicates → {1, 2, 3, 4}

print("My List =",my_list)
print("Converted My List to Set 'Unique' =",unique)






