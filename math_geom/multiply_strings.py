# https://leetcode.com/problems/multiply-strings

# TC - O(M*N), SC - O(M*N)
def multiply(num1: str, num2: str) -> str:
    # Handle edge case of zero
    if num1 == "0" or num2 == "0":
        return "0"

    # Initialize result array to store digits (reverse order for easier calculation)
    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    # Multiply each digit
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # Convert characters to integers
            digit1 = ord(num1[i]) - ord('0')
            digit2 = ord(num2[j]) - ord('0')

            # Multiply digits and add to result at appropriate position
            product = digit1 * digit2
            pos1, pos2 = i + j, i + j + 1
            product += result[pos2]

            # Update result array with carry
            result[pos2] = product % 10
            result[pos1] += product // 10

    # Convert result array to string, skipping leading zeros
    result_str = ""
    for digit in result:
        if not (result_str == "" and digit == 0):
            result_str += str(digit)

    # Return "0" if result is empty (happens if product is 0)
    return result_str if result_str else "0"

# Test cases
print(multiply("2", "3"))  # Output: "6"
print(multiply("123", "456"))  # Output: "56088"