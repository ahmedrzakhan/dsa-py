# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# TC - O(N), SC - O(min(M, N)), N is string length, M is length of unique chars
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  # To store characters in the current window
    max_length = 0    # To track the length of the longest valid substring
    L = 0          # Left pointer of the sliding window

    for R in range(len(s)):  # Iterate with right pointer
        while s[R] in char_set:  # If current char is already in set
            char_set.remove(s[L])  # Remove char at left pointer
            L += 1                # Shrink window from left
        char_set.add(s[R])       # Add current char to set
        max_length = max(max_length, R - L + 1)  # Update max length

    return max_length

print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))

# The time complexity is indeed O(N) because:

# The right pointer iterates N times.
# The left pointer moves at most N times in total.
# All set operations (add, remove, check) are O(1) on average.
# The total work is amortized to O(N), as each character is added and removed at most once.