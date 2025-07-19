a = 10
b = 3

print(a + b)     # 13 → addition
print(a - b)     # 7  → subtraction
print(a * b)     # 30 → multiplication
print(a / b)     # 3.333... → division (always float)
print(a // b)    # 3 → floor division (removes decimal)
print(a % b)     # 1 → remainder
print(a ** b)    # 1000 → 10^3

# Comparison

print(5 == 5)     # True
print(5 != 3)     # True
print(7 > 2)      # True
print(4 <= 4)     # True

# Logical Operators

print(a > 2 and a < 10)   # True (both conditions true)
print(a > 10 or a < 3)    # False (both false)
print(not (a > 2))        # False (opposite of True)

a = 5        # 0101
b = 3        # 0011

print(a & b)   # 1  → 0001
print(a | b)   # 7  → 0111
print(a ^ b)   # 6  → 0110 (exclusive OR)

if not (a&1):   # Check even odd in bit level
    print("Even")
else:
    print("Odd")

# Identity Check Operators

x = [1, 2]
y = [1, 2]
z = x

print(x == y)       # True (values same)
print(x is y)       # False (not same object)
print(x is z)       # True (same object)


