def maxArea(A):
    # Initialize two pointers: L at start, R at end
    L = 0
    R = len(A) - 1
    max_water = 0

    # Continue until pointers meet
    while L < R:
        # Calculate current water area
        # Width is distance between pointers (R - L)
        # Height is minimum of the two lines
        curr_water = min(A[L], A[R]) * (R - L)

        # Update max_water if current is larger
        max_water = max(max_water, curr_water)

        # Move the pointer pointing to the shorter line
        # Because moving the taller line inward won't increase area
        if A[L] < A[R]:
            L += 1
        else:
            R -= 1

    return max_water

# Test cases
print(maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(maxArea([1,1]))  # Output: 1