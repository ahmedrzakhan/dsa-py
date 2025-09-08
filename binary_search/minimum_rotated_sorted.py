# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# TC - O(LogN), SC - O(1)
def findMin(A):
    # If array has only one element, return it
    N = len(A)
    if N == 1:
        return A[0]

    L = 0
    R = len(A) - 1

    # If array is not rotated (last element >= first element)
    # then first element is minimum
    if A[R] > A[0]:
        return A[0]

    # Binary search
    while L <= R:
        mid = (L + R) // 2

        # Check if mid+1 is the minimum element
        # by comparing with mid # NOTE: mid < N-1 is bounds check
        if mid < N-1 and A[mid] > A[mid + 1]:
            return A[mid + 1]

        # Check if mid is the minimum element
        # by comparing with mid-1 # NOTE: mid > 0 is bounds check
        if mid > 0 and A[mid - 1] > A[mid]:
            return A[mid]

        # If mid element is greater than first element,
        # minimum lies in right half
        if A[mid] > A[L]:
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