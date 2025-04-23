# https://leetcode.com/problems/search-in-rotated-sorted-array/

# TC - O(N), SC - O(1)
def search(nums, target):
    L, R = 0, len(nums) - 1

    while L <= R:
        mid = (L + R) // 2

        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[L] <= nums[mid]:
            # Check if target is in left half
            if nums[L] <= target < nums[mid]:
                R = mid - 1
            else:
                L = mid + 1
        # right half is sorted
        else:
            # Check if target is in right half
            if nums[mid] < target <= nums[R]:
                L = mid + 1
            else:
                R = mid - 1

    return -1

# Test with the examples
print(search([4, 5, 6, 7, 0, 1, 2], 0))  # Expected: 4
print(search([4, 5, 6, 7, 0, 1, 2], 3))  # Expected: -1
print(search([1], 0))  # Expected: -1

# In nums[left] <= target < nums[mid]:
# <= includes nums[left] as a possible target value.
# < excludes nums[mid] since it’s checked separately.
# In nums[mid] < target <= nums[right]:
# < excludes nums[mid] since it’s checked separately.
# <= includes nums[right] as a possible target value.