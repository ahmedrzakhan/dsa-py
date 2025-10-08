# https://leetcode.com/problems/meeting-rooms/

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# TC - O(NLogN), SC - O(1)
def canAttendMeetings(A):
    # Determine if a person can attend all meetings without conflicts.
    # Args: intervals: List of Interval objects representing meeting times
    # Returns: bool: True if all meetings can be attended, False if there are conflicts
    # Handle edge cases
    if not A or len(A) <= 1:
        return True

    # Sort intervals by start time
    A.sort(key=lambda x: x.start)

    # Check for overlaps between adjacent meetings
    for i in range(1, len(A)):
        # If previous meeting ends after current meeting starts, there's a conflict
        if A[i].start < A[i-1].end:
            return False

    return True


# Test with the provided examples
def test_solution():
    # Example 1: Should return False
    intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    result1 = canAttendMeetings(intervals1)
    print(f"Example 1: [(0,30), (5,10), (15,20)]")
    print(f"Result: {result1}")
    print(f"Expected: False")
    print()

    # Example 2: Should return True
    intervals2 = [Interval(5, 8), Interval(9, 15)]
    result2 = canAttendMeetings(intervals2)
    print(f"Example 2: [(5,8), (9,15)]")
    print(f"Result: {result2}")
    print(f"Expected: True")
    print()

    # Additional test cases
    # Edge case: No meetings
    intervals3 = []
    result3 = canAttendMeetings(intervals3)
    print(f"Edge case (empty): []")
    print(f"Result: {result3}")
    print(f"Expected: True")
    print()

    # Edge case: One meeting
    intervals4 = [Interval(1, 5)]
    result4 = canAttendMeetings(intervals4)
    print(f"Edge case (single): [(1,5)]")
    print(f"Result: {result4}")
    print(f"Expected: True")
    print()

    # Back-to-back meetings (should not conflict)
    intervals5 = [Interval(0, 8), Interval(8, 10)]
    result5 = canAttendMeetings(intervals5)
    print(f"Back-to-back meetings: [(0,8), (8,10)]")
    print(f"Result: {result5}")
    print(f"Expected: True")
    print()

    # Multiple conflicts
    intervals6 = [Interval(1, 5), Interval(2, 6), Interval(3, 7)]
    result6 = canAttendMeetings(intervals6)
    print(f"Multiple conflicts: [(1,5), (2,6), (3,7)]")
    print(f"Result: {result6}")
    print(f"Expected: False")


if __name__ == "__main__":
    test_solution()