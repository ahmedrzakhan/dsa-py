def longestCommonSubsequence(text1: str, text2: str) -> int:
    # Bottom-up approach: Build DP table from the end of strings backwards.
    # Args: text1: First string
    #     text2: Second string
    # Returns: Length of the longest common subsequence
    L1, L2 = len(text1), len(text2)

    # Create DP table with (m+1) x (n+1) dimensions
    # dp[i][j] represents LCS length for text1[i:] and text2[j:]
    dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]

    # Fill the DP table from bottom-right to top-left
    for i in range(L1 - 1, -1, -1):
        for j in range(L2 - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]


# Test cases
def test_solution():
    # Example 1
    text1, text2 = "abcde", "ace"
    result = longestCommonSubsequence(text1, text2)
    print(f'Input: text1 = "{text1}", text2 = "{text2}"')
    print(f'Output: {result}')
    print(f'Expected: 3\n')

    # Example 2
    text1, text2 = "abc", "abc"
    result = longestCommonSubsequence(text1, text2)
    print(f'Input: text1 = "{text1}", text2 = "{text2}"')
    print(f'Output: {result}')
    print(f'Expected: 3\n')

    # Example 3
    text1, text2 = "abc", "def"
    result = longestCommonSubsequence(text1, text2)
    print(f'Input: text1 = "{text1}", text2 = "{text2}"')
    print(f'Output: {result}')
    print(f'Expected: 0\n')

    # Additional test case
    text1, text2 = "bsbininm", "jmjkbkjkv"
    result = longestCommonSubsequence(text1, text2)
    print(f'Input: text1 = "{text1}", text2 = "{text2}"')
    print(f'Output: {result}')

test_solution()