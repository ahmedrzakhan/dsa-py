# https://leetcode.com/problems/maximum-product-subarray

# TC - O(N), SC - O(1)
def maxProduct(A):
    if not A:
        return 0

    # Initialize current max, current min, and global max
    cur_max = cur_min = global_max = A[0]

    # Iterate through the array starting from the second element
    for ele in A[1:]:
        # Store current_max for use in min calculation
        temp_max = cur_max
        # Current max is the maximum of: current number, product with previous max, product with previous min
        cur_max = max(ele, cur_max * ele, cur_min * ele)
        # Current min is the minimum of: current number, product with previous max, product with previous min
        cur_min = min(ele, temp_max * ele, cur_min * ele)
        # Update global max if current max is larger
        global_max = max(global_max, cur_max)

    return global_max

# Example usage for local testing
# Test cases
print(maxProduct([2, 3, -2, 4]))  # Output: 6
print(maxProduct([-2, 0, -1]))    # Output: 0