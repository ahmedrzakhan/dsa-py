# https://leetcode.com/problems/valid-anagram/

# TC - O(N), SC - O(K)
def isAnagram(s: str, t: str) -> bool:
    # Check if lengths are different - if so, they can't be anagrams
    if len(s) != len(t):
        return False

    # Create an empty dictionary to store character counts
    char_count = {}

    # Count occurrences of each character in first string (s)
    for char in s:
        # Add 1 to existing count or start at 1 if char not seen before
        char_count[char] = char_count.get(char, 0) + 1

    # Check second string (t) against character counts
    for char in t:
        # If char not in dictionary or its count is already 0, not an anagram
        if char not in char_count or char_count[char] == 0:
            return False
        # Decrease count by 1 for each matching character found
        char_count[char] -= 1

    # If we get here, all characters matched with correct frequencies
    return True

# Example 1
print(isAnagram("anagram", "nagaram"))  # Output: True

# Example 2
print(isAnagram("rat", "car"))          # Output: False