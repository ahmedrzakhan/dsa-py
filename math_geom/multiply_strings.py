# https://leetcode.com/problems/multiply-strings

# TC - O(M*N), SC - O(M*N)
def multiply(num1: str, num2: str) -> str:
    # Handle edge case: if either number is "0", result is "0"
    if "0" in [num1, num2]:
        return "0"

    # Initialize result array with zeros
    # Maximum possible length is len(num1) + len(num2)
    # Example: 99 * 99 = 9801 (2 digits + 2 digits = 4 digits max)
    res = [0] * (len(num1) + len(num2))

    # Reverse both strings to process from least significant digit first
    # This makes indexing easier for positional multiplication
    num1, num2 = num1[::-1], num2[::-1]

    # Nested loop to multiply each digit of num1 with each digit of num2
    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            # Multiply current digits
            digit = int(num1[i1]) * int(num2[i2])

            # Add the product to the appropriate position in result array
            # Position i1 + i2 is where this multiplication contributes
            res[i1 + i2] += digit

            # Handle carry: move tens digit to next position
            res[i1 + i2 + 1] += res[i1 + i2] // 10

            # Keep only units digit in current position
            res[i1 + i2] = res[i1 + i2] % 10

    # Post-process the result array
    # Reverse back to get most significant digit first
    res = res[::-1]

    # Find the first non-zero digit to remove leading zeros
    beg = 0
    while beg < len(res) and res[beg] == 0:
        beg += 1

    # Convert remaining digits to strings and join them
    # res[beg:] removes leading zeros
    res = map(str, res[beg:])
    return "".join(res)

# Test cases
# print(multiply("2", "3"))      # Output: "6"
print(multiply("123", "456"))  # Output: "56088"