name = "Joha"               # Double quotes
dept = 'EEE'                # Single quotes

info = """This is a
multi-line string"""       # Triple quotes for multiple lines

print(name[0])    # Prints "J"
print(name[1])    # Prints "or"
print(name[-1])    # Prints "a"
print(name[-2])    # Prints "h"


# String Slicing 

text = "Python"

print(text[1:4])   # 'yth' (from index 1 to 3)
print(text[:3])    # 'Pyt' (start to index 2)
print(text[3:])    # 'hon' (from index 3 to end)
print(text[-3:])   # 'hon' (prints last three)

st = " Hey, I am Joha."

print(st.strip())    # Removes Spaces from start and end
print(len(st))       # Length with spaces
print(st.upper())    # Makes everything upoercase, use lower() for lowercase 
print(st.replace("Hey","Hola")) # Replace the slice with smth else

print("Hey" in st)       # True → checks if "Hey" is in the string
print("i" not in st)   # True → case-sensitive

age = 22
print("I am " + str(age) + " years old")    # Convert number to string

pi = 3.1415926535

print(f"Pi = {pi:.2f}")       # 2 decimal places → Pi = 3.14
print(f"Pi = {pi:.4f}")       # 4 decimal places → Pi = 3.1416

