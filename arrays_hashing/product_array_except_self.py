# https://leetcode.com/problems/product-of-array-except-self/description/

# TC - O(N), SC - O(1)
def productExceptSelf(nums):
    n = len(nums)
    # Initialize output array
    answer = [1] * n

    # First pass: compute products of all elements to the left of each element
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Second pass: multiply by products of all elements to the right of each element
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

# Test cases
print(productExceptSelf([1,2,3,4]))        # Output: [24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3]))    # Output: [0,0,9,0,0]