# https://leetcode.com/problems/word-break

# TC - O(N^2*K), SC - O(N+M)
def wordBreak(S: str, wordDict: list[str]) -> bool:
    # Create a set for O(1) lookup
    word_set = set(wordDict)
    # dp[i] represents whether s[0:i] can be segmented
    DP = [False] * (len(S) + 1)
    # Empty string is always valid
    DP[0] = True

    # Iterate through each position in string
    for i in range(1, len(S) + 1):
        # Check all possible prefixes ending at i
        for j in range(i):
            # If prefix s[0:j] is valid and s[j:i] is in dictionary
            if DP[j] and S[j:i] in word_set:
                DP[i] = True
                break

    return DP[len(S)]

# Test cases
test_cases = [
    ("leetcode", ["leet", "code"]),
    ("applepenapple", ["apple", "pen"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"])
]

for s, wordDict in test_cases:
    result = wordBreak(s, wordDict)
    print(f"Input: s = \"{s}\", wordDict = {wordDict}")
    print(f"Output: {result}\n")