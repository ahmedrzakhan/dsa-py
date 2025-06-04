# https://leetcode.com/problems/number-of-1-bits

# TC - O(N), SC - O(1)
def hammingWeight(n: int) -> int:
    # Optimized bitwise approach
    count = 0
    while n:
        count += n & 1  # Check least significant bit
        n >>= 1        # Right shift by 1
    return count

# Test cases
test_cases = [
    (11, 3),          # Binary: 1011
    (128, 1),         # Binary: 10000000
    (2147483645, 30)  # Binary: 1111111111111111111111111111101
]

for input_n, expected in test_cases:
    result = hammingWeight(input_n)
    print(f"Input: {input_n}, Output: {result}, Expected: {expected}, {'Pass' if result == expected else 'Fail'}")
