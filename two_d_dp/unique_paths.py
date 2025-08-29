# https://leetcode.com/problems/unique-paths/

# TC - O(M*N), SC - O(N)
def uniquePaths(m: int, n: int) -> int:
    # Initialize the first row with all 1s (base case: only one way to reach any cell in first row)
    prev_row = [1] * n

    # For each subsequent row
    for _ in range(m - 1):
        # Create a new row, starting with 1 (base case: only one way to reach leftmost cell)
        curr_row = [1] * n

        # For each column (except the first), calculate paths by adding:
        # - paths from cell above (next_row[col_index])
        # - paths from cell to the left (current_row[col_index])
        for j in range(n - 2, -1, -1):
            curr_row[j] = curr_row[j + 1] + prev_row[j]

        # Move to the next row
        prev_row = curr_row

    # Return the number of paths to reach the bottom-right corner
    return prev_row[0]


# Test case 1
m, n = 3, 7
result1 = uniquePaths(m, n)
print(f"Test 1 - m={m}, n={n}")
print(f"DP 1D: {result1}")
print(f"Expected: 28\n")

# Test case 2
m, n = 3, 2
result1 = uniquePaths(m, n)
print(f"Test 2 - m={m}, n={n}")
print(f"DP 1D: {result1}")
print(f"Expected: 3\n")

# Test edge cases
m, n = 1, 1
result = uniquePaths(m, n)
print(f"Edge case - m={m}, n={n}: {result} (Expected: 1)")

m, n = 1, 10
result = uniquePaths(m, n)
print(f"Edge case - m={m}, n={n}: {result} (Expected: 1)")
