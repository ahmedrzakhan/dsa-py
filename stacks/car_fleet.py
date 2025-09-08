# https://leetcode.com/problems/car-fleet/description/

from typing import List

# TC - O(NlogN), SC - O(N)
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    # Create list of tuples with (position, speed) pairs using list comprehension
    # zip() pairs up corresponding elements from position and speed lists
    pair = list(zip(position, speed))

    # Sort pairs in descending order by position
    # This processes cars from right (closest to target) to left
    pair.sort(reverse=True)

    # Initialize empty stack to store arrival times of fleets
    stack = []

    # Iterate through sorted (position, speed) pairs
    for p, s in pair:
        # Calculate time to reach target: (distance to target) / speed
        # Add this arrival time to the stack
        stack.append((target - p) / s)

        # Check if current car catches up to previous fleet
        # Need at least 2 times in stack to compare
        # If current arrival time <= previous fleet's time, they merge
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            # Remove current car's time since it joins the previous fleet
            # Previous fleet's time remains as it determines fleet speed
            stack.pop()

    # Return number of fleets
    # Length of stack equals number of distinct fleets reaching target
    return len(stack)

# Test cases with different scenarios
test_cases = [
    (12, [10,8,0,5,3], [2,4,1,1,3]),  # Multiple fleets example
    (10, [3], [3]),                    # Single car example
    (100, [0,2,4], [4,2,1])           # All cars merge into one fleet
]

# Execute and print results for each test case
for target, position, speed in test_cases:
    result = carFleet(target, position, speed)
    print(f"Target: {target}, Position: {position}, Speed: {speed}")
    print(f"Number of fleets: {result}\n")