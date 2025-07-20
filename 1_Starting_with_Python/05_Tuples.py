# Tuples are list, But Tuples are immutable

point = (10, 20)              # A tuple with two numbers
colors = ("red", "green", "blue")  # A tuple of strings

# Can't change anything here

print(point[0])               # First item → 10
print(colors[-1])             # Last item → "blue"

y = (5,)       # This is a tuple with one item

student = ("Joha", 22, "EEE")     # A tuple with name, age, and dept
print(student[0])                 # Print name → "Joha"
# student[1] = 23                # This will throw error, Tuples are immutable


