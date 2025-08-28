# https://leetcode.com/problems/non-overlapping-intervals/

# TC - O(NLogN), SC - O(1)
def eraseOverlapIntervals(intervals):
    # Return minimum number of intervals to remove to make rest non-overlapping.
    # Strategy: Greedy approach - sort by end time and keep intervals that don't overlap.
    # This maximizes the number of intervals we keep, minimizing removals.
    # Time: O(n log n) for sorting
    # Space: O(1) excluding input
    if not intervals:
        return 0

    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])

    count = 0  # Number of intervals to remove
    last_item = intervals[0][1]  # End time of last kept interval

    # Start from second interval
    for i in range(1, len(intervals)):
        start, end = intervals[i]

        if start < last_item:  # Overlapping interval found
            count += 1
        else:
            # Non-overlapping, update prev_end
            last_item = end

    return count

# Test cases
def test_solution():
    # Example 1: [[1,2],[2,3],[3,4],[1,3]] -> 1
    # After sorting by end: [[1,2],[2,3],[1,3],[3,4]]
    # Keep [1,2], [2,3], [3,4]. Remove [1,3]
    intervals1 = [[1,2],[2,3],[3,4],[1,3]]
    result1 = eraseOverlapIntervals(intervals1)
    print(f"Example 1: {intervals1} -> {result1}")

    # Example 2: [[1,2],[1,2],[1,2]] -> 2
    # All same, keep one, remove two
    intervals2 = [[1,2],[1,2],[1,2]]
    result2 = eraseOverlapIntervals(intervals2)
    print(f"Example 2: {intervals2} -> {result2}")

    # Example 3: [[1,2],[2,3]] -> 0
    # Already non-overlapping (touching at point is allowed)
    intervals3 = [[1,2],[2,3]]
    result3 = eraseOverlapIntervals(intervals3)
    print(f"Example 3: {intervals3} -> {result3}")

    # Edge case: single interval
    intervals4 = [[1,2]]
    result4 = eraseOverlapIntervals(intervals4)
    print(f"Single interval: {intervals4} -> {result4}")

    # Complex case
    intervals5 = [[1,4],[2,3],[3,4],[1,2]]
    result5 = eraseOverlapIntervals(intervals5)
    print(f"Complex case: {intervals5} -> {result5}")

test_solution()