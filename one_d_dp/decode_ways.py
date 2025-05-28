# https://leetcode.com/problems/decode-ways/description/

# TC - O(N), SC - O(N)
def numDecodings(S: str) -> int:
    if not S or S[0] == '0':
        return 0

    N = len(S)
    DP = [0] * (N + 1)
    DP[0] = 1  # Empty string has 1 way
    DP[1] = 1  # First character has 1 way if it's not '0'

    for i in range(2, N + 1):
        # Check if single digit is valid
        if S[i-1] != '0':
            DP[i] += DP[i-1]

        # Check if two-digit number is valid (between 10 and 26)
        two_digit = int(S[i-2:i])
        if 10 <= two_digit <= 26:
            DP[i] += DP[i-2]

    return DP[N]

# Test cases for local execution
test_cases = ["12", "226", "06", "121321"]
for test in test_cases:
    print(f"Input: {test}, Output: {numDecodings(test)}")