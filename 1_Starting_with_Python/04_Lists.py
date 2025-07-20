fruits = ["apple", "banana", "mango"]  # Create a list of strings
numbers = [10, 20, 30, 40]             # A list of integers
mixed = [1, "hello", 3.5]              # A mixed list

print(fruits[0])      # Access the first item: "apple"
print(fruits[-1])     # Access the last item: "mango", -1 means first from last

fruits[1] = "orange"   # Replace "banana" with "orange"
print(fruits)          # Output: ['apple', 'orange', 'mango']

fruits.append("grape")     # Add to the end
fruits.insert(1, "lemon")  # Insert at index 1, so list is now ['apple', 'lemon', 'orange', 'mango', 'grape']

print(fruits)

fruits.remove("apple")     # Removes the first occurrence of "apple"
fruits.pop()               # Removes the last item

print(fruits)              # ['lemon', 'orange', 'mango']

print("================================================================")

#===================================================================================================

numbers = [4, 2, 9, 1]
print(len(numbers))      # Number of items → 4
print(sum(numbers))      # Sum of items → 16
print(min(numbers))      # Smallest → 1
print(max(numbers))      # Largest → 9

numbers.pop(2)           # Removes 9

print(numbers)

squares = [x**2 for x in range(1, 6)]   # [1, 4, 9, 16, 25]

print(squares)

squares2 = []
for x in range(1, 6):
    squares2.append(x**2)

