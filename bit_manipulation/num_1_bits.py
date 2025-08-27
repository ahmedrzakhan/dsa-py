# https://leetcode.com/problems/number-of-1-bits

# TC - O(N), SC - O(1)
def hammingWeight(n: int) -> int:
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        # i >> 1 is equivalent to i // 2
        # i & 1 checks if i is odd (adds 1 if odd, 0 if even)
        ans[i] = ans[i >> 1] + (i & 1)

    return ans

# Test cases
test_cases = [
    (11, 3),          # Binary: 1011
    (128, 1),         # Binary: 10000000
    (2147483645, 30)  # Binary: 1111111111111111111111111111101
]

for input_n, expected in test_cases:
    result = hammingWeight(input_n)
    print(f"Input: {input_n}, Output: {result}, Expected: {expected}, {'Pass' if result == expected else 'Fail'}")
