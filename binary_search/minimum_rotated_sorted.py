# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# TC - O(N), SC - O(1)
def findMin(nums):
    # If array has only one element, return it
    if len(nums) == 1:
        return nums[0]

    L = 0
    R = len(nums) - 1

    # If array is not rotated (last element >= first element)
    # then first element is minimum
    if nums[R] > nums[0]:
        return nums[0]

    # Binary search
    while L <= R:
        mid = (L + R) // 2

        # Check if mid+1 is the minimum element
        # by comparing with mid
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        # Check if mid is the minimum element
        # by comparing with mid-1
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # If mid element is greater than first element,
        # minimum lies in right half
        if nums[mid] > nums[0]:
            L = mid + 1
        # If mid element is less than first element,
        # minimum lies in left half
        else:
            R = mid - 1

# Test cases
test_cases = [
    [3,4,5,1,2],
    [4,5,6,7,0,1,2],
    [11,13,15,17]
]

for nums in test_cases:
    result = findMin(nums)
    print(f"Input: {nums}")
    print(f"Minimum: {result}\n")