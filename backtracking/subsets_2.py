# https://leetcode.com/problems/subsets-ii/

# TC - O(N*2^N), SC - O(N)
def subsetsWithDup(nums):
    """
    Generate all possible subsets without duplicates from an array that may contain duplicates.

    Args:
        nums: List of integers that may contain duplicates

    Returns:
        List of lists representing all unique subsets
    """
    result = []
    nums.sort()  # Sort to handle duplicates easily

    def backtrack(start, curSet):
        # Add current subset to result
        result.append(curSet[:])  # Make a copy

        # Try adding each remaining element
        for i in range(start, len(nums)):
            # Skip duplicates: if current element equals previous element
            # and we're not at the start position, skip it
            if i > start and nums[i] == nums[i-1]:
                continue

            # Include current element
            curSet.append(nums[i])
            # Recurse with next position
            backtrack(i + 1, curSet)
            # Backtrack: remove current element
            curSet.pop()

    backtrack(0, [])
    return result


def test_solution():
    """Test the solution with provided examples"""

    # Test case 1
    nums1 = [1, 2, 2]
    result1 = subsetsWithDup(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]")
    print()

    # Test case 2
    nums2 = [0]
    result2 = subsetsWithDup(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [[], [0]]")
    print()

    # Additional test case with more duplicates
    nums3 = [4, 4, 4, 1, 4]
    result3 = subsetsWithDup(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print()

    # Test case with negative numbers
    nums4 = [-1, -1, 2]
    result4 = subsetsWithDup(nums4)
    print(f"Input: {nums4}")
    print(f"Output: {result4}")


test_solution()