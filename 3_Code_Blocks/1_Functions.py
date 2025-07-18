# Define a function named 'greet' that takes one parameter 'name'
def greet(name):
    print("Hello,", name)  # Print a greeting message

# Call the function with the argument 'Alice'
greet("Alice")  # Output: Hello, Alice

# Define a function to add two numbers
def add(a, b):
    return a + b  # Return the sum of a and b

# Call the add function and store the result
result = add(5, 3)  

print("Sum:", result)  # Print the result

def greet(name="XYZ"):          # Default value is "XYZ" if no input given
    print("Hello,", name)

greet()                            # Output: Hello, XYZ
greet("Joha")                      # Output: Hello, Joha
