# https://leetcode.com/problems/valid-palindrome/description/

# TC - O(N), SC - O(N)
def isPalindrome(s: str) -> bool:
    # Clean the string
    cleaned = ''
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    # Compare with its reverse
    return cleaned == cleaned[::-1]


test_cases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " "
]

for test in test_cases:
    print(f"Input: {test}")
    print(f"Output: {isPalindrome(test)}\n")