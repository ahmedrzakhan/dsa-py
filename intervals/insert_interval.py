# https://leetcode.com/problems/insert-interval/

# TC - O(N), SC - O(1)
def insert(A, newInterval):
    # Insert newInterval into intervals, merging overlapping intervals.
    # Args: intervals: List of non-overlapping intervals sorted by start time
    #     newInterval: Interval to insert [start, end]
    # Returns: List of intervals after insertion and merging
    result = []
    i = 0
    N = len(A)

    # Add all intervals that end before newInterval starts
    while i < N and A[i][1] < newInterval[0]:
        result.append(A[i])
        i += 1

    # Merge overlapping intervals with newInterval
    # Update newInterval's bounds to include all overlapping intervals
    while i < N and A[i][0] <= newInterval[1]:
        # Merge: take minimum start and maximum end
        newInterval[0] = min(newInterval[0], A[i][0])
        newInterval[1] = max(newInterval[1], A[i][1])
        i += 1

    # Add the merged interval
    result.append(newInterval)

    # Add all remaining intervals
    while i < N:
        result.append(A[i])
        i += 1

    return result


# Test cases
def test_insert():
    # Example 1
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    result1 = insert(intervals1, newInterval1)
    print(f"Example 1: {result1}")
    # Expected: [[1,5],[6,9]]

    # Example 2
    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    result2 = insert(intervals2, newInterval2)
    print(f"Example 2: {result2}")
    # Expected: [[1,2],[3,10],[12,16]]

    # Edge cases
    print("\nEdge cases:")

    # Empty intervals
    result3 = insert([], [5,7])
    print(f"Empty intervals: {result3}")
    # Expected: [[5,7]]

    # New interval doesn't overlap with any
    result4 = insert([[1,2],[4,5]], [6,8])
    print(f"No overlap: {result4}")
    # Expected: [[1,2],[4,5],[6,8]]

    # New interval overlaps with all
    result5 = insert([[1,2],[3,4],[5,6]], [0,7])
    print(f"Overlaps all: {result5}")
    # Expected: [[0,7]]

    # Insert at beginning
    result6 = insert([[3,5],[6,9]], [1,2])
    print(f"Insert at beginning: {result6}")
    # Expected: [[1,2],[3,5],[6,9]]

test_insert()