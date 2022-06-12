# Bit-wise operators.
# A brief lecture on the meaning of the bitwise operators.

# Complement operator ~
print(~12) # Used to store negative numbers.

# Bitwise '&'
print(12 & 13)
# Is the logical AND comparison of the numbers in binary notation.
# 12 -> 0 0 0 0 1 1 0 0
# 13 -> 0 0 0 0 1 1 0 1
# ----------------------
#       0 0 0 0 1 1 0 0 -> 12 

# Bitwise '|'
print(12 | 13)
# Is the logical OR comparison of the numbers in binary notation.
# 12 -> 0 0 0 0 1 1 0 0
# 13 -> 0 0 0 0 1 1 0 1
# ----------------------
#       0 0 0 0 1 1 0 1 -> 13

# Bitwise XOR '^'
print(12 ^ 13)
# Is the logical XOR comparison of the numbers in binary notation.
# 12 -> 0 0 0 0 1 1 0 0
# 13 -> 0 0 0 0 1 1 0 1
# ----------------------
#       0 0 0 0 0 0 0 1 -> 1

# Left-shift
print(10 << 2) # Adding two zeros-bits to the left of the number.

# Right-shift
print(10 >> 2) # Trimming two zeros-bits to the right of the numb