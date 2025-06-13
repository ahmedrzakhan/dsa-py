# https://leetcode.com/problems/plus-one

# TC - O(N), SC - O(1)
def plusOne(digits):
    N = len(digits)

    # Start from the least significant digit
    for i in range(N - 1, -1, -1):
        # If digit is less than 9, increment and return
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If digit is 9, set to 0 and continue (carry over)
        digits[i] = 0

    # If we get here, all digits were 9
    return [1] + [0] * N

# Test case 1
print(plusOne([1, 2, 3]))  # Expected: [1, 2, 4]

# # Test case 2
print(plusOne([4, 3, 2, 1]))  # Expected: [4, 3, 2, 2]

# Test case 3
print(plusOne([9, 9]))  # Expected: [1, 0]