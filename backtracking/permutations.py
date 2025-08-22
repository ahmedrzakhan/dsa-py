# https://leetcode.com/problems/permutations/

# TC - O(N*2^N), SC - O(N)
def permute(nums):
    """
    Generate all possible permutations of distinct integers.

    Args:
        nums: List of distinct integers

    Returns:
        List of all permutations, where each permutation is a list
    """
    result = []

    def backtrack(curr_set):
        # Base case: if current permutation has all elements
        if len(curr_set) == len(nums):
            result.append(curr_set[:])  # Add a copy
            return

        # Try each unused number / Skip if number is already used
        for num in nums:
            if num not in curr_set:
                # Choose / Add current number to permutation
                curr_set.append(num)
                # Explore / Recurse with updated permutation
                backtrack(curr_set)
                # Unchoose (backtrack) / Backtrack by removing the number
                curr_set.pop()

    backtrack([])
    return result

def test_permutations():
    """Test the permutation functions with the given examples."""

    # Test cases from the problem
    test_cases = [
        [1, 2, 3],
        [0, 1],
        [1]
    ]

    expected_results = [
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
        [[0,1],[1,0]],
        [[1]]
    ]

    print("Testing Permutations Function")
    print("=" * 50)

    for i, test_case in enumerate(test_cases):
        print(f"\nTest Case {i+1}: {test_case}")

        # Test both implementations
        result1 = permute(test_case.copy())

        print(f"Result (backtrack): {result1}")

        # Verify results match expected (order may differ)
        expected = expected_results[i]
        if len(result1) == len(expected) and all(perm in expected for perm in result1):
            print("✓ PASSED")
        else:
            print("✗ FAILED")

    # Additional test with larger array
    print(f"\nAdditional Test: [1,2,3,4] (should have 24 permutations)")
    result = permute([1,2,3,4])
    print(f"Number of permutations: {len(result)}")
    print(f"First few: {result[:6]}")


# Run tests
test_permutations()

# Interactive example
print("\n" + "="*50)
print("Interactive Example:")
nums = [1, 2, 3]
result = permute(nums)
print(f"All permutations of {nums}:")
for i, perm in enumerate(result, 1):
    print(f"{i}. {perm}")