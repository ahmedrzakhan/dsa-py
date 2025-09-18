# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque

# TC - O(N), SC - O(N)
def maxSlidingWindow(A, k):
    if not A or k == 0:
        return []

    # Deque stores indices of array elements in decreasing order of their values
    dq = deque()
    result = []

    for i in range(len(A)):
        # Remove indices that are out of current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove indices whose corresponding values are smaller than current element
        # This maintains decreasing order in deque
        while dq and A[dq[-1]] <= A[i]:
            dq.pop()

        # Add current element's index
        dq.append(i)

        # If we have processed at least k elements, add max to result
        if i >= k - 1:
            result.append(A[dq[0]])  # Front of deque has max element's index

    return result

# Test with provided examples
def test_solution():
    # Example 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    result1 = maxSlidingWindow(nums1, k1)
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected: [3, 3, 5, 5, 6, 7]")
    print(f"Correct: {result1 == [3, 3, 5, 5, 6, 7]}\n")

    # Example 2
    nums2 = [1]
    k2 = 1
    result2 = maxSlidingWindow(nums2, k2)
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected: [1]")
    print(f"Correct: {result2 == [1]}\n")

    # Additional test case
    nums3 = [9, 10, 9, -7, -4, -8, 2, -6]
    k3 = 5
    result3 = maxSlidingWindow(nums3, k3)
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {result3}")
    print(f"Expected: [10, 10, 9, 2]")

# Run tests
test_solution()