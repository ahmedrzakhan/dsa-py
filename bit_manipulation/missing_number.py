# https://leetcode.com/problems/missing-number

# Approach 1: Mathematical Sum Formula
# Time: O(n), Space: O(1)
# The sum of numbers from 0 to n is n*(n+1)/2
# Missing number = expected_sum - actual_sum
# n = len(nums)
# expected_sum = n * (n + 1) // 2
# actual_sum = sum(nums)
# return expected_sum - actual_sum

# TC - O(N), SC - O(1)
def missingNumber(nums):
    n = len(nums)
    result = n  # Start with n

    for i in range(n):
        result ^= i ^ nums[i]

    return result

# Test cases
print(missingNumber([3, 0, 1]) == 2)
print(missingNumber([0, 1]) == 2)
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8)

# Key Idea: XOR Properties
# The solution leverages two key properties of the XOR operation (^):

# Self-cancellation: a ^ a = 0 (a number XORed with itself is 0).
# Zero XOR: a ^ 0 = a (a number XORed with 0 is itself).
# Associativity and commutativity: The order of XOR operations doesn’t matter.