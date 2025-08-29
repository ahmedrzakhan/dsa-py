# https://leetcode.com/problems/interleaving-string/

# TC - O(M*N), SC - O(M*N)
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    DP = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    DP[len(s1)][len(s2)] = True

    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i + j] and DP[i + 1][j]:
                DP[i][j] = True
            if j < len(s2) and s2[j] == s3[i + j] and DP[i][j + 1]:
                DP[i][j] = True
    return DP[0][0]


# Test cases
# Test case 1
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(f"Test 1: {isInterleave(s1, s2, s3)}")  # Expected: True

# Test case 2
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(f"Test 2: {isInterleave(s1, s2, s3)}")  # Expected: False

# Test case 3
s1 = ""
s2 = ""
s3 = ""
print(f"Test 3: {isInterleave(s1, s2, s3)}")  # Expected: True

# Additional test case
s1 = "ab"
s2 = "cd"
s3 = "acbd"
print(f"Test 4: {isInterleave(s1, s2, s3)}")  # Expected: True
