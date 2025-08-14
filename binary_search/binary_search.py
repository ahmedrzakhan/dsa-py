# https://leetcode.com/problems/binary-search/description/

# TC - O(LogN), SC -O(1)
def search(A, target):
    L = 0
    R = len(A) - 1

    while L <= R:
        mid = (L + R) // 2

        # If target is found at mid, return the index
        if A[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif A[mid] < target:
            L = mid + 1

        # If target is smaller, ignore right half
        else:
            R = mid - 1

    # Target not found
    return -1

# Test cases
print(search([-1,0,3,5,9,12], 9))  # Output: 4
print(search([-1,0,3,5,9,12], 2))  # Output: -1