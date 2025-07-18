# Famous syntax range(start, stop, step)

for i in range(5):      # Prints 0 to 4 (Excludes upper limit, lower limit by default 1)
    print(i)

for i in range(2,6):    # Prints 2 to 6
    print(i)

for i in range(1, 10, 2):   # Prints 1 3 5 7 9
    print(i)

for ch in "Joha":          # Go through each character in the string "Joha"
    print(ch, end = " ")   
    
    """ Print the current character, end = " " forces 
    the print function not create a newline 
    by default, puts an whitespace """         # A risky way to do commenting btw TwT

