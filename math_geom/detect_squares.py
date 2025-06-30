# https://leetcode.com/problems/detect-squares

from collections import Counter  # Import Counter for counting point occurrences
from typing import List

# TC - O(1)/O(N), SC - O(N)
# Class to detect and count axis-aligned squares formed by points in a 2D plane
class DetectSquares:
    def __init__(self):
        # Initialize a Counter to store the frequency of each point (x, y) as a tuple
        # Counter automatically initializes missing keys to 0 when accessed
        self.pts_count = Counter()
        # Initialize a list to store all points for iteration in count method
        self.pts = []

    def add(self, point: List[int]) -> None:
        # Add a point to the data structure
        # Increment the count of the point (converted to tuple) in pts_count
        self.pts_count[tuple(point)] += 1
        # Append the point (as a list) to the pts list for iteration
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        # Initialize result to store the total number of valid squares
        res = 0
        # Extract x and y coordinates of the query point
        px, py = point
        # Iterate over all stored points in pts
        for x, y in self.pts:
            # Skip points that cannot form a valid square:
            # 1. If the horizontal and vertical distances are not equal (not a square)
            # 2. If x == px (same x-coordinate, zero side length)
            # 3. If y == py (same y-coordinate, zero side length)
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            # For a valid square with (px, py) and (x, y) as diagonal corners,
            # check the other two corners: (x, py) and (px, y)
            # Multiply their frequencies to get the number of squares for this configuration
            res += self.pts_count[(x, py)] * self.pts_count[(px, y)]
        # Return the total number of valid squares
        return res

detect_squares = DetectSquares()
detect_squares.add([3, 10])
detect_squares.add([11, 2])
detect_squares.add([3, 2])
print(detect_squares.count([11, 10]))  # Should print 1
print(detect_squares.count([14, 8]))   # Should print 0
detect_squares.add([11, 2])
print(detect_squares.count([11, 10]))  # Should print 2