# https://leetcode.com/problems/missing-number

# TC - O(N), SC - O(1)
def missingNumber(nums):
    missing = len(nums)  # Initialize with n (length of array)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

# Test cases
print(missingNumber([3, 0, 1]) == 2)
print(missingNumber([0, 1]) == 2)
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8)

# Key Idea: XOR Properties
# The solution leverages two key properties of the XOR operation (^):

# Self-cancellation: a ^ a = 0 (a number XORed with itself is 0).
# Zero XOR: a ^ 0 = a (a number XORed with 0 is itself).
# Associativity and commutativity: The order of XOR operations doesn’t matter.