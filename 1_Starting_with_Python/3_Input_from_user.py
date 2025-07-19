name = input("What is your name? ")
print("Hello,", name)

# Python treats input as string by default

age = int(input("Enter Your Age: "))    # Convert to int upon taking input

print("Hello," + name + ".You are", age,"years old.")   # In case of string, we can concatenate using + instead of comma

x,y = input("Enter two Numbers: ").split()
x = int(x)       # Convert first input
y = int(y)       # Convert second input
print(f"Sum = {x + y}")

# This is random example that you can do it too

print("Hi joha, Your id is: ",input("Enter your id: "))    # input() will be executed first in this line
