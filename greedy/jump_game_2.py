# https://leetcode.com/problems/jump-game-ii

# TC - O(N), SC - O(1)
def jump(A):
    N = len(A)
    if N <= 1:
        return 0

    jumps = 0
    current_end = 0  # Current jump range end
    farthest = 0     # Farthest reachable index

    # Iterate until we reach or pass the last index
    for i in range(N - 1):
        # Update farthest reachable index
        farthest = max(farthest, i + A[i])

        # If we reach the current jump range end
        if i == current_end:
            jumps += 1
            current_end = farthest

            # Early termination if we can reach the end
            if current_end >= N - 1:
                break

    return jumps

# Test cases
# Test case 1
nums1 = [2,3,1,1,4]
print(f"Test case 1: {jump(nums1)}")  # Expected: 2

# Test case 2
nums2 = [2,3,0,1,4]
print(f"Test case 2: {jump(nums2)}")  # Expected: 2