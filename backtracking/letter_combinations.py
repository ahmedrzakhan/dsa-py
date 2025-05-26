# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# TC - O(4^N), SC - O(N)
def letterCombinations(digits):
    if not digits:
        return []

    # Phone number mapping
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []

    def backtrack(index, current):
        # If we've processed all digits, add combination to result
        if index == len(digits):
            result.append(current)
            return

        # Get letters for current digit
        letters = phone_map[digits[index]]

        # Try each letter for current digit
        for letter in letters:
            backtrack(index + 1, current + letter)

    backtrack(0, "")
    return result

# Test cases
# Test case 1
print(letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Test case 2
print(letterCombinations(""))  # []

# Test case 3
print(letterCombinations("2"))  # ["a","b","c"]