# https://leetcode.com/problems/longest-palindromic-substring/description/

# TC - O(N^2), SC - O(1)
def longestPalindrome(s):
    if not s:
        return ""

    # Initialize variables to track the start and end of the longest palindrome
    start = 0
    max_length = 1

    def expand_around_center(L, R):
        # Expand around the center while characters match and indices are valid
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        # Return the length and starting index of the palindrome
        # (L + 1) because L is one step beyond the palindrome
        return R - L - 1, L + 1

    # Iterate through each possible center position
    for i in range(len(s)):
        # Check for odd-length palindromes (single character center)
        length1, start1 = expand_around_center(i, i)
        # Check for even-length palindromes (between i and i+1)
        length2, start2 = expand_around_center(i, i + 1)

        # Update if we find a longer palindrome
        if length1 > max_length:
            start = start1
            max_length = length1
        if length2 > max_length:
            start = start2
            max_length = length2

    # Return the substring from start to start + max_length
    return s[start:start + max_length]

# Example usage for local testing
# Test cases
test_cases = ["babad", "cbbd", "a", "racecar", ""]
for s in test_cases:
    result = longestPalindrome(s)
    print(f"Input: {s}, Output: {result}")