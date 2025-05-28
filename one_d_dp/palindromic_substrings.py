# TC - O(N^2), SC - O(1)
def countSubstrings(s):
    def count_palindromes(L, R):
        count = 0
        # Expand around center while within bounds and characters match
        while L >= 0 and R < len(s) and s[L] == s[R]:
            count += 1
            L -= 1
            R += 1
        return count

    total = 0
    # Check each position as a potential center
    for i in range(len(s)):
        # Odd-length palindromes (center at i)
        total += count_palindromes(i, i)
        # Even-length palindromes (center between i and i+1)
        total += count_palindromes(i, i + 1)

    return total

# Test cases
print(countSubstrings("abc"))  # Output: 3
print(countSubstrings("aaa"))  # Output: 6