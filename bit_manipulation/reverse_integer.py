# https://leetcode.com/problems/reverse-integer/

# TC - O(1), SC - O(1)
def reverse(x: int) -> int:
    # Handle the sign
    sign = 1 if x >= 0 else -1
    x = abs(x)

    # Reverse digits by converting to string and back
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    # Apply sign
    reversed_num *= sign

    # Check for 32-bit integer overflow
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0

    return reversed_num

print(reverse(123))  # Output: 321
print(reverse(-123))  # Output: -321
print(reverse(120))  # Output: 21