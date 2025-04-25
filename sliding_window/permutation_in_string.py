# https://leetcode.com/problems/permutation-in-string/description/

# TC - O(N), SC - O(1)
def checkInclusion(s1: str, s2: str) -> bool:
    # If s1 is longer than s2, no permutation can exist
    if len(s1) > len(s2):
        return False

    # Initialize frequency arrays for s1 and the sliding window
    s1_count = [0] * 26
    window_count = [0] * 26

    # Count frequencies of characters in s1 and first window of s2
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1
        window_count[ord(s2[i]) - ord('a')] += 1

    # Check if the first window matches
    if s1_count == window_count:
        return True

    # Slide the window over s2
    for i in range(len(s1), len(s2)):
        # Add new character to the window
        window_count[ord(s2[i]) - ord('a')] += 1
        # Remove character from the start of the previous window
        window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
        # Check if current window matches s1's frequency
        if s1_count == window_count:
            return True

    return False


print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))

