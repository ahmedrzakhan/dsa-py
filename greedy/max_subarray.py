# https://leetcode.com/problems/maximum-subarray/

# TC - O(N), SC - O(1)
def maxSubArray(nums):
    max_sum = nums[0]  # Initialize with first element
    current_sum = nums[0]  # Track current subarray sum

    for num in nums[1:]:
        # For each number, decide whether to start new subarray or extend existing
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test cases
def test_max_subarray():
    # Test case 1
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6, "Test case 1 failed"
    # Test case 2
    assert maxSubArray([1]) == 1, "Test case 2 failed"
    # Test case 3
    assert maxSubArray([5,4,-1,7,8]) == 23, "Test case 3 failed"
    print("All test cases passed!")

test_max_subarray()