# https://leetcode.com/problems/valid-anagram/

# TC - O(N), SC - O(K)
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0)+1

    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -=1

    return True

# Example 1
print(isAnagram("anagram", "nagaram"))  # Output: True

# Example 2
print(isAnagram("rat", "car"))          # Output: False