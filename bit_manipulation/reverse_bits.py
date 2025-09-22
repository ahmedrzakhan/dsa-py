# https://leetcode.com/problems/reverse-bits

# TC - O(1), SC - O(1)
def reverseBits(n: int) -> int:
    # Reverse bits of a given 32-bit unsigned integer.
    # Args: n: 32-bit unsigned integer
    # Returns: 32-bit unsigned integer with bits reversed
    result = 0

    # Process all 32 bits
    for _ in range(32):
        # Extract the least significant bit of n
        bit = n & 1

        # Shift result left and add the extracted bit
        result = (result << 1) | bit

        # Shift n right to process the next bit
        n >>= 1

    return result

# Test cases
print(reverseBits(43261596))  # Should output 964176192
print(reverseBits(4294967293))  # Should output 3221225471
