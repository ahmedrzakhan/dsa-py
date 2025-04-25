# https://leetcode.com/problems/longest-repeating-character-replacement/description/
# TC - O(N), SC - O(1)
def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_len = 0
    L = 0

    for R in range(len(s)):
        # Update character count
        count[s[R]] = count.get(s[R], 0) + 1

        # Window size minus most frequent char count gives replacements needed
        window_size = R - L + 1
        max_count = max(count.values())
        replacements = window_size - max_count

        # If replacements needed exceed k, shrink window
        if replacements > k:
            count[s[L]] -= 1
            L += 1

        # Update max length
        max_len = max(max_len, R - L + 1)

    return max_len

print(characterReplacement("ABAB", 2))