# https://leetcode.com/problems/trapping-rain-water

# TC - O(N), SC - O(1)
def trap_water(A):
    if not A or len(A) < 3:
        return 0

    L, R = 0, len(A) - 1
    leftMax, rightMax = A[L], A[R]
    res = 0
    while L < R:
        if leftMax < rightMax:
            L += 1
            leftMax = max(leftMax, A[L])
            res += leftMax - A[L]
        else:
            R -= 1
            rightMax = max(rightMax, A[R])
            res += rightMax - A[R]
    return res

# Test the solutions
def test_solutions():
    test_cases = [
        [0,1,0,2,1,0,1,3,2,1,2,1],  # Expected: 6
        [4,2,0,3,2,5],               # Expected: 9
        [3,0,2,0,4],                 # Expected: 7
        [0,1,0,1,0],                 # Expected: 1
        [5,4,1,2],                   # Expected: 1
        [1,2,3,4,5],                 # Expected: 0 (no trapping)
        [5,4,3,2,1],                 # Expected: 0 (no trapping)
        []                           # Expected: 0 (empty)
    ]

    solutions = [
        ("Two Pointers", trap_water),
    ]

    for i, test_case in enumerate(test_cases):
        print(f"Test case {i + 1}: {test_case}")
        for name, func in solutions:
            result = func(test_case)
            print(f"  {name}: {result}")
        print()


test_solutions()

# Demonstrate with the main examples
print("=== Main Examples ===")
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]

print(f"Example 1: {height1}")
print(f"Result: {trap_water(height1)} units")
print()

print(f"Example 2: {height2}")
print(f"Result: {trap_water(height2)} units")