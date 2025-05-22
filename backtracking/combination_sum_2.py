# https://leetcode.com/problems/combination-sum-ii

# TC - O(2^N), SC - O(N)
def combinationSum2(A, target):
    """
    Find all unique combinations where candidate numbers sum to target.
    Each number may only be used once.

    Args:
        candidates: List of integers (may contain duplicates)
        target: Target sum

    Returns:
        List of all unique combinations that sum to target
    """
    def backtrack(start, curSet, curSum):
        # Base case: if we've reached the target sum
        if curSum == target:
            result.append(curSet[:])  # Add a copy of the current combination
            return

        # If current sum exceeds target, stop exploring this path
        if curSum > target:
            return

        # Try each candidate starting from 'start' index
        for i in range(start, len(A)):
            # Skip duplicates: if current element is same as previous, skip it
            # This prevents duplicate combinations
            if i > start and A[i] == A[i - 1]:
                continue

            # Include the current candidate
            curSet.append(A[i])

            # Recursively explore with the next index (i+1, not i)
            # This ensures each element is used only once
            backtrack(i + 1, curSet, curSum + A[i])

            # Backtrack: remove the last added candidate
            curSet.pop()

    # Sort A to handle duplicates properly
    A.sort()
    result = []
    backtrack(0, [], 0)
    return result


# Test function with examples
def test_combination_sum2():
    # Example 1
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    result1 = combinationSum2(candidates1, target1)
    print(f"Example 1:")
    print(f"Input: candidates = {candidates1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Expected: [[1,1,6],[1,2,5],[1,7],[2,6]]")
    print()

    # Example 2
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    result2 = combinationSum2(candidates2, target2)
    print(f"Example 2:")
    print(f"Input: candidates = {candidates2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Expected: [[1,2,2],[5]]")
    print()

    # Additional test case with all same numbers
    candidates3 = [1, 1, 1, 1, 1]
    target3 = 3
    result3 = combinationSum2(candidates3, target3)
    print(f"Example 3 (Additional):")
    print(f"Input: candidates = {candidates3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Expected: [[1,1,1]]")
    print()

    # Edge case: no valid combinations
    candidates4 = [3, 5, 7]
    target4 = 2
    result4 = combinationSum2(candidates4, target4)
    print(f"Example 4 (Edge case):")
    print(f"Input: candidates = {candidates4}, target = {target4}")
    print(f"Output: {result4}")
    print(f"Expected: []")


def demonstrate_algorithm():
    """Demonstrate how the algorithm works step by step"""
    print("\n" + "="*60)
    print("ALGORITHM DEMONSTRATION")
    print("="*60)

    candidates = [1, 1, 2, 5, 6]
    target = 8

    print(f"\nInput: candidates = {candidates}, target = {target}")
    print("\nAfter sorting: [1, 1, 2, 5, 6]")
    print("\nExploration process:")
    print("- Start with 1 (index 0)")
    print("  - Add second 1 (index 1)")
    print("    - Add 2: [1,1,2] = 4")
    print("      - Add 5: [1,1,2,5] = 9 (exceeds target, backtrack)")
    print("    - Skip 5, add 6: [1,1,6] = 8 ✓ (found solution!)")
    print("  - Skip second 1 (duplicate at same level)")
    print("  - Add 2: [1,2] = 3")
    print("    - Add 5: [1,2,5] = 8 ✓ (found solution!)")
    print("- Skip second 1 (start from index 1, but it's duplicate)")
    print("- Start with 2 (index 2)")
    print("  - Add 5: [2,5] = 7")
    print("    - Add 6: [2,5,6] = 13 (exceeds target, backtrack)")
    print("  - Add 6: [2,6] = 8 ✓ (found solution!)")
    print("... and so on")

    result = combinationSum2(candidates, target)
    print(f"\nFinal result: {result}")


test_combination_sum2()

print("\n" + "="*60 + "\n")

demonstrate_algorithm()

print("\n" + "="*60 + "\n")
print("Test with your own input:")

# Example custom test
custom_candidates = [1, 2, 2, 2, 5]
custom_target = 5
custom_result = combinationSum2(custom_candidates, custom_target)
print(f"Input: candidates = {custom_candidates}, target = {custom_target}")
print(f"Output: {custom_result}")