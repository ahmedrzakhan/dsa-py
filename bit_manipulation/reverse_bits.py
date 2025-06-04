# https://leetcode.com/problems/reverse-bits

# TC - O(1), SC - O(1)
def reverseBits(n: int) -> int:
    result = 0
    for i in range(32):
        # Get the i-th bit from n
        bit = (n >> i) & 1
        # Place it at the (31-i)-th position in result
        result |= (bit << (31 - i))
    return result

# Test cases
print(reverseBits(43261596))  # Should output 964176192
print(reverseBits(4294967293))  # Should output 3221225471

# Summary
# The reverseBits function reverses the 32-bit binary representation of an integer by:

# Extracting each bit using right shift and AND.
# Placing it in the mirrored position using left shift and OR.
# Processing all 32 bits in a fixed loop.

# In the reverseBits function, the goal is to reverse the 32-bit binary representation of an integer n.
# For each bit at position i (0 to 31, from least to most significant) in n, we want to place it at position
# 31 - i in result. For example:

# The bit at position 0 (least significant) in n should go to position 31 (most significant) in result.
# The bit at position 1 in n should go to position 30 in result, and so on.
# Explanation of the Line
# The line result |= (bit << (31 - i)) does the following:

# Extracted Bit:
# bit is the i-th bit of n, obtained earlier via (n >> i) & 1. It’s either 0 or 1.
# Left Shift (bit << (31 - i)):
# The << operator shifts the bits of bit left by 31 - i positions.
# If bit = 1, then 1 << (31 - i) creates a number with a 1 in position 31 - i and 0s elsewhere.
# If bit = 0, then 0 << (31 - i) results in 0 (no change needed).
# For example:
# If i = 0, then 31 - i = 31. So, bit << 31 shifts bit to the 31st position (most significant bit).
# If i = 2, then 31 - i = 29. So, bit << 29 shifts bit to the 29th position.
# Bitwise OR (result |= ...):
# The |= operator performs a bitwise OR between result and the shifted bit, updating result.
# This sets the bit at position 31 - i in result to the value of bit (0 or 1) without affecting other
# bits in result.
# For example, if result is currently 000...000 and bit << (31 - i) is 100...000 (1 in position 31), the OR
# operation sets position 31 in result to 1.
# Example
# Let’s use the test case n = 43261596 (binary: 00000010100101000001111010011100) and focus on one iteration,
# say i = 2.

# Extract the bit:
# bit = (n >> 2) & 1:
# Right shift n by 2: 00000010100101000001111010011100 >> 2 = 00000010100101000001111010011.
# Least significant bit is 1, so bit = 1.
# Place in mirrored position:
# i = 2, so 31 - i = 29.
# bit << (31 - i) = 1 << 29:
# This shifts the bit 1 left by 29 positions, resulting in 00100000000000000000000000000000 (a 1 in position
# 29, 0s elsewhere).
# In decimal, 1 << 29 = 2^29 = 536870912.
# Update result:
# result |= 536870912:
# If result was previously 000...000, after the OR, it becomes 00100000000000000000000000000000 (1 in position 29).
# If other bits were already set in result, they remain unchanged because OR with 0 doesn’t alter bits.
# This process "mirrors" the bit: the bit at position 2 in n is placed at position 29 in result.

# Why "Mirrored"?
# The term "mirrored" refers to the reversal of bit positions:

# Position 0 ↔ Position 31
# Position 1 ↔ Position 30
# Position 2 ↔ Position 29
# And so on. The expression 31 - i calculates the mirrored position for bit i in a 32-bit integer.
# Visualizing with the Example
# For n = 43261596:

# Binary: 00000010100101000001111010011100.
# At i = 2, the bit is 1 (third bit from the right).
# This 1 is placed at position 29 in result, contributing to the reversed binary:
# 00111001011110000010100101000000.
# Why Use Left Shift and OR?
# Left Shift: Positions the bit exactly where it needs to go in the reversed order.
# OR: Safely sets the bit in result without disturbing other bits, as OR with 0 leaves bits unchanged,
# and OR with 1 sets the bit to 1.
# Summary
# "Placing it in the mirrored position using left shift and OR" means taking the extracted bit, shifting
# it left to its reversed position (31 - i) in the 32-bit integer, and using the OR operation to set that bit
# in result. This ensures each bit from the input is correctly placed in the mirrored position of the output,
# building the reversed binary representation one bit at a time.