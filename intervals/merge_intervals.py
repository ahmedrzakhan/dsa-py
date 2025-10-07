# https://leetcode.com/problems/merge-intervals/description/

# TC - O(NLogN), SC - O(1)
def merge(A):
    # Merge all overlapping intervals and return non-overlapping intervals.
    # Args: intervals: List of intervals where each interval is [start, end]
    # Returns: List of merged non-overlapping intervals
    if not A:
        return []

    # Sort intervals by start time
    A.sort()

    result = [A[0]]

    for curr in A[1:]:
        last_item = result[-1]

        # If current interval overlaps with the last merged interval
        if curr[0] <= last_item[1]:
            # Merge by updating the end time to the maximum of both ends
            last_item[1] = max(last_item[1], curr[1])
        else:
            # No overlap, add current interval to result
            result.append(curr)

    return result


# Test cases
def test_merge():
    # Example 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    result1 = merge(intervals1)
    print(f"Input: {intervals1}")
    print(f"Output: {result1}")
    print(f"Expected: [[1,6],[8,10],[15,18]]\n")

    # Example 2
    intervals2 = [[1,4],[4,5]]
    result2 = merge(intervals2)
    print(f"Input: {intervals2}")
    print(f"Output: {result2}")
    print(f"Expected: [[1,5]]\n")

    # Edge cases
    intervals3 = [[1,4],[0,4]]
    result3 = merge(intervals3)
    print(f"Input: {intervals3}")
    print(f"Output: {result3}")
    print(f"Expected: [[0,4]]\n")

    intervals4 = [[1,4],[2,3]]
    result4 = merge(intervals4)
    print(f"Input: {intervals4}")
    print(f"Output: {result4}")
    print(f"Expected: [[1,4]]\n")

# Run tests
test_merge()