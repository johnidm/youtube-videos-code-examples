# Define two numbers
a = 5   # Binary: 0101
b = 3   # Binary: 0011

# Perform XOR operation
result = a ^ b

print(f"a: {a} (binary: {bin(a)})")
print(f"b: {b} (binary: {bin(b)})")
print(f"a XOR b: {result} (binary: {bin(result)})")

# Explanation of the bitwise operation:
# 0101
# 0011
# -----
# 0110 -> This is the binary result for 6 in decimal.
# In this example, 5 in binary is 0101 and 3 in binary is 0011. Performing XOR on these gives us:
# - The first bit: 0 XOR 0 = 0
# - The second bit: 1 XOR 0 = 1
# - The third bit: 0 XOR 1 = 1
# - The fourth bit: 1 XOR 1 = 0
# The result is 0110, which is 6 in decimal.

# Use Cases:
# Swapping Values: You can use XOR to swap two variables without needing a temporary variable.

x, y = 5, 7

result = x ^ y
print(f"Before swap: x={x}, y={y}")
print(f"Binary values: x={bin(x)}, y={bin(y)}")
print(f"a XOR b: {result} (binary: {bin(result)})")
# Swapping using XOR
x ^= y
y ^= x
x ^= y

print(f"After swap: x={x}, y={y}")

# Finding Unique Number: If an array contains all elements twice except one, the XOR of all elements will yield the unique number.
nums = [4, 1, 2, 1, 2]
unique_number = 0
for num in nums:
    unique_number ^= num

print(f"Unique number: {unique_number}")
