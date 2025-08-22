# https://leetcode.com/problems/jump-game/

# TC -O(N), SC - O(1)
def canJump(A):
    max_reach = 0  # Tracks the furthest index we can reach

    for i in range(len(A)):
        # If we can't reach the current index, return False
        if i > max_reach:
            return False
        # Update the furthest we can reach from current position
        max_reach = max(max_reach, i + A[i])
        # If we can reach or pass the last index, return True
        if max_reach >= len(A) - 1:
            return True

# Test cases
# Example 1
nums1 = [2, 3, 1, 1, 4]
print(f"Example 1: {canJump(nums1)}")  # Should print True

# Example 2
nums2 = [3, 2, 1, 0, 4]
print(f"Example 2: {canJump(nums2)}")  # Should print False


# If you can reach a given position (e.g., if you're at index 3 but max_reach is only 2, you know you're stuck).