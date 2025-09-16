# https://leetcode.com/problems/largest-rectangle-in-histogram/

# TC - O(N), SC - O(N)
def largestRectangleArea(A):
    maxArea = 0
    stack = []  # pair: (index, height)
    N = len(A)

    for i, h in enumerate(A):
        start = i
        while stack and  h < stack[-1][1] :
            idx, height = stack.pop()
            maxArea = max(maxArea, height * (i - idx))
            start = idx
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (N - i))

    return maxArea


# Test with the provided examples
def test_solution():
    # Example 1
    heights1 = [2, 1, 5, 6, 2, 3]
    result1 = largestRectangleArea(heights1)
    print(f"Example 1: heights = {heights1}")
    print(f"Output: {result1}")
    print(f"Expected: 10")
    print()

    # Example 2
    heights2 = [2, 4]
    result2 = largestRectangleArea(heights2)
    print(f"Example 2: heights = {heights2}")
    print(f"Output: {result2}")
    print(f"Expected: 4")
    print()

    # Additional test cases
    test_cases = [
        ([1], 1),
        ([0], 0),
        ([2, 2, 2], 6),
        ([1, 2, 3, 4, 5], 9),
        ([5, 4, 3, 2, 1], 9),
        ([6, 2, 5, 4, 5, 1, 6], 12)
    ]

    print("Additional test cases:")
    for i, (heights, expected) in enumerate(test_cases):
        result = largestRectangleArea(heights)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {heights} -> {result} (expected {expected}) {status}")


test_solution()