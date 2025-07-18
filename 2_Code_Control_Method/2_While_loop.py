i = 1
while i <= 50:
    print(i)
    i += 1  # or i = i + 1

# Now a code to keep taking input using while

password = ""

while password != "Joha8888":       # Keep running until password variable is not Joha8888
    password = input("Enter password: ")

    if password != "Joha8888":
        print("Wrong Password!")

print("Access granted!")            # If you can get out of the loop, it'll be executed
