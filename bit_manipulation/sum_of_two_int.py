# https://leetcode.com/problems/sum-of-two-integers/

# TC - O(1), SC - O(1)
def getSum(a: int, b: int) -> int:
    # 32-bit mask to simulate 32-bit integer arithmetic
    mask = 0xFFFFFFFF
    # Maximum positive value for a 32-bit signed integer
    max_int = 0x7FFFFFFF

    while b != 0:
        # Step 1: Find all positions where both bits are 1 (these will create carries)
        carry_positions = a & b

        # Step 2: Shift carries left by 1 (carry goes to next higher bit)
        carry = carry_positions << 1

        # Step 3: Add without carry (XOR gives sum without carry)
        a = (a ^ b) & mask  # Keep result in 32 bits

        # Step 4: The carry becomes our new 'b' for next iteration
        b = carry & mask    # Keep carry in 32 bits

    # Handle signed integer conversion:
    # If result fits in positive 32-bit range, return as-is
    # Otherwise, convert to negative by flipping bits relative to 32-bit boundary
    return a if a <= max_int else ~(a ^ mask)


# print(getSum(1, 2) == 3)
# print(getSum(2, 3) == 5)
print(getSum(-2, 3) == 1)
print(getSum(-1000, -1000) == -2000)
print(getSum(0, 0) == 0)