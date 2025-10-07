# https://leetcode.com/problems/meeting-rooms-ii

import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# TC - O(NLogN), SC - O(N)
def min_meeting_rooms(A):
    if not A:
        return 0

    # Sort meetings by start time
    A.sort(key=lambda x: x.start)

    # Min heap to track end times of ongoing meetings
    min_heap = []

    for interval in A:
        # Remove meetings that have ended before current meeting starts
        while min_heap and min_heap[0] <= interval.start:
            heapq.heappop(min_heap)

        # Add current meeting's end time
        heapq.heappush(min_heap, interval.end)

    return len(min_heap)


# Test cases
def test_solution():
    # Test case 1
    intervals1 = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    result1 = min_meeting_rooms(intervals1)
    print(f"Test 1: [(0,40), (5,10), (15,20)]")
    print(f"Result: {result1} rooms")
    print(f"Expected: 2 rooms")
    print()

    # Test case 2
    intervals2 = [Interval(4, 9)]
    result2 = min_meeting_rooms(intervals2)
    print(f"Test 2: [(4,9)]")
    print(f"Result: {result2} room")
    print(f"Expected: 1 room")
    print()

    # Additional test cases
    intervals3 = [Interval(0, 8), Interval(8, 10)]  # No conflict at boundary
    result3 = min_meeting_rooms(intervals3)
    print(f"Test 3: [(0,8), (8,10)]")
    print(f"Result: {result3} room")
    print(f"Expected: 1 room (no conflict at boundary)")
    print()

    intervals4 = [Interval(1, 3), Interval(2, 4), Interval(3, 6)]
    result4 = min_meeting_rooms(intervals4)
    print(f"Test 4: [(1,3), (2,4), (3,6)]")
    print(f"Result: {result4} rooms")
    print()

    intervals5 = []  # Empty case
    result5 = min_meeting_rooms(intervals5)
    print(f"Test 5: []")
    print(f"Result: {result5} rooms")
    print(f"Expected: 0 rooms")

if __name__ == "__main__":
    test_solution()