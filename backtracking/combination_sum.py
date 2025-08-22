# https://leetcode.com/problems/combination-sum/description/

# TC - O(N^T/M) where N is the number of candidates, T is the target value, and M is the minimal value among the candidates
# SC - O(T/M)

def combinationSum(A, target):
    """
    Find all unique combinations of candidates that sum to target.

    Args:
        candidates: List of distinct integers
        target: Target sum

    Returns:
        List of all unique combinations that sum to target
    """
    def backtrack(start, curr_set, curr_sum):
        # Base case: if we've reached the target sum
        if curr_sum == target:
            result.append(curr_set[:])  # Add a copy of the current combination
            return

        # If current sum exceeds target, stop exploring this path
        if curr_sum > target:
            return

        # Try each candidate starting from 'start' index
        for i in range(start, len(A)):
            # Include the current candidate
            curr_set.append(A[i])

            # Recursively explore with the same starting index (allowing reuse)
            backtrack(i, curr_set, curr_sum + A[i])

            # Backtrack: remove the last added candidate
            curr_set.pop()

    result = []
    backtrack(0, [], 0)
    return result


# Test function with examples
def test_combination_sum():
    # Example 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    result1 = combinationSum(candidates1, target1)
    print(f"Example 1:")
    print(f"Input: candidates = {candidates1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Expected: [[2,2,3],[7]]")
    print()

    # Example 2
    candidates2 = [2, 3, 5]
    target2 = 8
    result2 = combinationSum(candidates2, target2)
    print(f"Example 2:")
    print(f"Input: candidates = {candidates2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Expected: [[2,2,2,2],[2,3,3],[3,5]]")
    print()

    # Example 3
    candidates3 = [2]
    target3 = 1
    result3 = combinationSum(candidates3, target3)
    print(f"Example 3:")
    print(f"Input: candidates = {candidates3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Expected: []")


test_combination_sum()

# You can also test with your own input
# print("\n" + "="*50 + "\n")
# print("Test with your own input:")

# # Example custom test
# custom_candidates = [2, 3, 4, 5]
# custom_target = 10
# custom_result = combinationSum(custom_candidates, custom_target)
# print(f"Input: candidates = {custom_candidates}, target = {custom_target}")
# print(f"Output: {custom_result}")