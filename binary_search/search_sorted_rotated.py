# https://leetcode.com/problems/search-in-rotated-sorted-array/

# TC - O(N), SC - O(1)
def search(A, target):
    L, R = 0, len(A) - 1

    while L <= R:
        mid = (L + R) // 2

        if A[mid] == target:
            return mid

        # Check if left half is sorted
        if A[L] <= A[mid]:
            # Check if target is in left half
            if A[L] <= target < A[mid]:
                R = mid - 1
            else:
                L = mid + 1
        # right half is sorted
        else:
            # Check if target is in right half
            if A[mid] < target <= A[R]:
                L = mid + 1
            else:
                R = mid - 1

    return -1

# Test with the examples
print(search([4, 5, 6, 7, 0, 1, 2], 0))  # Expected: 4
print(search([4, 5, 6, 7, 0, 1, 2], 3))  # Expected: -1
print(search([1], 0))  # Expected: -1

# In A[left] <= target < A[mid]:
# <= includes A[left] as a possible target value.
# < excludes A[mid] since it’s checked separately.
# In A[mid] < target <= A[right]:
# < excludes A[mid] since it’s checked separately.
# <= includes A[right] as a possible target value.