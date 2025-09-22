# https://leetcode.com/problems/counting-bits/

# TC - O(NLogN), SC - O(1)
def countBits(n):
    # Initialize empty list to store bit counts for each number from 0 to n
    ans = []

    # Iterate through each number from 0 to n (inclusive)
    for i in range(n + 1):
        # Initialize counter for 1-bits in current number
        count = 0
        # Copy current number to avoid modifying loop variable
        num = i

        # Count 1-bits by examining each bit position
        while num:
            # Check if least significant bit is 1 and add to count
            # num & 1 returns 1 if LSB is 1, otherwise 0
            count += num & 1
            # Right shift by 1 bit to examine next bit position
            # Equivalent to integer division by 2
            num >>= 1

        # Store the count of 1-bits for current number
        ans.append(count)

    return ans

# Example usage
# Test cases
# print(countBits(2))  # Output: [0, 1, 1]
print(countBits(5))  # Output: [0, 1, 1, 2, 1, 2]

# This refers to a clever bitwise operation used to count the number of 1’s in the binary
# representation of a number i. The approach relies on the property that performing a bitwise
# AND between i and i-1 removes the rightmost 1 in i’s binary form. By reusing the count of 1’s
# for the resulting number (stored in a dynamic programming array), we add 1 to account for the removed bit.

# Explanation with an Example
# Let’s take i = 5 as an example and walk through how this works.

# Binary Representation of i:
# The number 5 in binary is 101, which has two 1’s.
# Compute i-1:
# i-1 = 5 - 1 = 4.
# In binary, 4 is 100.
# Perform i & (i-1):
# Compute the bitwise AND of i (5) and i-1 (4):
# 101 (5) AND 100 (4) = 100 (4).
# Notice that 100 (4) is the binary representation of 5 (101) with its rightmost 1 removed.
# Count the 1’s:
# The number i & (i-1) = 4 (100) has one 1 in its binary form (assuming we already computed
# this in our dynamic programming array ans[4] = 1).
# Since i & (i-1) removed one 1 from i, the number of 1’s in i is:
# Number of 1’s in i & (i-1) + 1 = ans[4] + 1 = 1 + 1 = 2.
# So, ans[5] = 2, which matches the number of 1’s in 101.
# Why Does i & (i-1) Remove the Rightmost 1?
# The operation i & (i-1) works because subtracting 1 from a number flips its rightmost 1 to
# 0 and sets all bits to its right to 1. When you perform a bitwise AND between i and i-1, the
# rightmost 1 in i is ANDed with a 0, turning it to 0, while other bits are preserved where both have 1’s.

# Let’s try another example with i = 6:

# Binary Representation:
# 6 in binary is 110 (two 1’s).
# Compute i-1:
# i-1 = 6 - 1 = 5, which is 101 in binary.
# Perform i & (i-1):
# 110 (6) AND 101 (5) = 100 (4).
# The rightmost 1 in 110 is removed, resulting in 100.
# Count the 1’s:
# The number i & (i-1) = 4 (100) has one 1 (assume ans[4] = 1 from prior computation).
# Number of 1’s in 6 = ans[4] + 1 = 1 + 1 = 2.
# This matches the two 1’s in 110.
# How This Fits in the Code
# In the dynamic programming solution, we store the number of 1’s for each number in the array ans.
# For a given i, we compute ans[i] using ans[i & (i-1)] + 1. Since i & (i-1) is a smaller number
# (already processed in the loop), we reuse its result and add 1 for the bit that was removed.
# This avoids recalculating the bit count from scratch and achieves O(n) time complexity, as each
# number is processed once with constant-time bitwise operations.

# Visual Example for Clarity
# For n = 5, the array ans is built as follows:

# ans[0] = 0 (binary 0, 0 ones).
# i = 1: Binary 1, 1 & (1-1) = 1 & 0 = 0, ans[1] = ans[0] + 1 = 0 + 1 = 1.
# i = 2: Binary 10, 2 & (2-1) = 2 & 1 = 10 & 01 = 00 = 0, ans[2] = ans[0] + 1 = 0 + 1 = 1.
# i = 3: Binary 11, 3 & (3-1) = 3 & 2 = 11 & 10 = 10 = 2, ans[3] = ans[2] + 1 = 1 + 1 = 2.
# i = 4: Binary 100, 4 & (4-1) = 4 & 3 = 100 & 011 = 000 = 0, ans[4] = ans[0] + 1 = 0 + 1 = 1.
# i = 5: Binary 101, 5 & (5-1) = 5 & 4 = 101 & 100 = 100 = 4, ans[5] = ans[4] + 1 = 1 + 1 = 2.
# Final output: [0, 1, 1, 2, 1, 2].

# This approach is efficient because it builds the solution iteratively, reusing results and avoiding
# explicit bit counting, satisfying the problem’s constraints and follow-up requirements.