# https://leetcode.com/problems/jump-game-ii

# TC - O(N), SC - O(1)
def jump(A):
    res = 0
    L, R = 0, 0

    while R < len(A) - 1:
        farthest = 0
        for i in range(L, R + 1):
            farthest = max(farthest, i + A[i])
        L = R + 1
        R = farthest
        res += 1
    return res

# Test cases
# Test case 1
nums1 = [2,3,1,1,4]
print(f"Test case 1: {jump(nums1)}")  # Expected: 2

# Test case 2
nums2 = [2,3,0,1,4]
print(f"Test case 2: {jump(nums2)}")  # Expected: 2