# https://leetcode.com/problems/binary-search/description/

# TC - O(N), SC -O(1)
def search(nums, target):
    L = 0
    R = len(nums) - 1

    while L <= R:
        mid = (L + R) // 2

        # If target is found at mid, return the index
        if nums[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif nums[mid] < target:
            L = mid + 1

        # If target is smaller, ignore right half
        else:
            R = mid - 1

    # Target not found
    return -1

# Test cases
print(search([-1,0,3,5,9,12], 9))  # Output: 4
print(search([-1,0,3,5,9,12], 2))  # Output: -1