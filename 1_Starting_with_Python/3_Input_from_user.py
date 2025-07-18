name = input("What is your name? ")
print("Hello,", name)

# Python treats input as string by default

age = int(input("Enter Your Age: "))    # Convert to int upon taking input

print("Hello," + name + ".You are", age,"years old.")   # In case of string, we can concatenate using + instead of comma
