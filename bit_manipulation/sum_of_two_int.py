# TC - O(1), SC - O(1)
def getSum(a: int, b: int) -> int:
    mask = 0xffffffff  # 32-bit mask to simulate 32-bit integer arithmetic (2^32 - 1)

    while (b & mask) > 0:  # Continue loop while there is a carry bit
        carry = ((a & b) << 1) & mask  # Calculate carry by ANDing a and b, shifting left, and masking
        a = (a ^ b) & mask  # Compute sum without carry using XOR, then mask to 32 bits
        b = carry  # Update b with the carry for the next iteration

    return a if a <= 0x7fffffff else (a | ~mask)  # Return a if positive or within 32-bit signed range, otherwise adjust for negative


# print(getSum(1, 2) == 3)
# print(getSum(2, 3) == 5)
print(getSum(-2, 3) == 1)
print(getSum(-1000, -1000) == -2000)
print(getSum(0, 0) == 0)