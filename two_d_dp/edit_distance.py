# https://leetcode.com/problems/edit-distance/

# TC: O(m * n),  SC: O(m * n) where m = len(s1), n = len(s2)
def minDistance(s1: str, s2: str) -> int:
    # Calculate the minimum edit distance between two strings.
    # Uses bottom-up dynamic programming, building from the end of strings backward.
    # cache[i][j] represents min operations to convert s1[i:] to s2[j:]

    # Initialize cache with infinity values
    DP = [[float("inf")] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Base cases: converting remaining s2 to empty string
    for j in range(len(s2) + 1):
        DP[len(s1)][j] = len(s2) - j

    # Base cases: converting remaining s1 to empty string
    for i in range(len(s1) + 1):
        DP[i][len(s2)] = len(s1) - i

    # Fill DP from bottom-right to top-left
    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2) - 1, -1, -1):
            if s1[i] == s2[j]:
                # Characters match, no operation needed
                DP[i][j] = DP[i + 1][j + 1]
            else:
                # Take minimum of three operations:
                # 1. Delete from s1: DP[i + 1][j] + 1
                # 2. Insert into s1: DP[i][j + 1] + 1
                # 3. Replace in s1: DP[i + 1][j + 1] + 1
                DP[i][j] = 1 + min(DP[i + 1][j], DP[i][j + 1], DP[i + 1][j + 1])

    return DP[0][0]


# Test cases
# Test case 1
s1, s2 = "horse", "ros"
result = minDistance(s1, s2)
print(f"minDistance('{s1}', '{s2}') = {result}")
print("Expected: 3")
print()

# Test case 2
s1, s2 = "intention", "execution"
result = minDistance(s1, s2)
print(f"minDistance('{s1}', '{s2}') = {result}")
print("Expected: 5")
print()

# Test edge cases
test_cases = [
    ("", "abc"),      # Empty to non-empty
    ("abc", ""),      # Non-empty to empty
    ("", ""),         # Both empty
    ("same", "same"), # Identical strings
    ("a", "b"),       # Single character replacement
    ("cat", "dog"),   # Complete replacement
]

print("Additional test cases:")
for w1, w2 in test_cases:
    result1 = minDistance(w1, w2)
    print(f"'{w1}' -> '{w2}': {result1}")

