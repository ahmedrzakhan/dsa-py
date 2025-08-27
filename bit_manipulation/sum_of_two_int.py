# https://leetcode.com/problems/sum-of-two-integers/

# TC - O(1), SC - O(1)
def getSum(a: int, b: int) -> int:
    # 32-bit mask to simulate 32-bit integer arithmetic
    mask = 0xFFFFFFFF
    # Maximum positive value for a 32-bit signed integer
    max_int = 0x7FFFFFFF

    # Perform addition using bitwise operations (no + operator)
    while b != 0:
        # Calculate carry bits: where both a and b have 1s, shifted left by 1
        carry = (a & b) << 1

        # XOR gives sum without carry, mask ensures 32-bit bounds
        a = (a ^ b) & mask

        # Update b to be the carry for next iteration, mask ensures 32-bit bounds
        b = carry & mask

    # Handle signed integer conversion:
    # If result fits in positive 32-bit range, return as-is
    # Otherwise, convert to negative by flipping bits relative to 32-bit boundary
    return a if a <= max_int else ~(a ^ mask)


# print(getSum(1, 2) == 3)
# print(getSum(2, 3) == 5)
print(getSum(-2, 3) == 1)
print(getSum(-1000, -1000) == -2000)
print(getSum(0, 0) == 0)