# https://leetcode.com/problems/find-the-duplicate-number/description/

# TC - O(N), SC - O(1)
def findDuplicate(nums: list[int]) -> int:
    # Floyd's Tortoise and Hare (Cycle Detection)
    # Initialize tortoise and hare
    slow = 0
    fast = 0

    # Phase 1: Find intersection point of tortoise and hare
    while True:
        slow = nums[slow] # Move one step
        fast = nums[nums[fast]] # Move two steps
        if slow == fast:
            break

    # Phase 2: Find entrance to the cycle
    fast = 0
    while True:
        slow = nums[slow]  # Move one step
        fast = nums[fast]          # Move one step
        if slow == fast:
            return slow

# Test cases
print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(findDuplicate([3, 1, 3, 4, 2]))  # Output: 3
print(findDuplicate([3, 3, 3, 3, 3]))  # Output: 3


# Problem Understanding
# Given an array nums of length n + 1 with integers in [1, n].
# Exactly one number is repeated (appears two or more times).
# We must find the repeated number without modifying the array and using O(1) extra space.
# Why it works:

# Since all values are between 1 and n, and array indices are 0 to n, the values will always point to valid indices (when used as indices)
# The duplicate number creates a cycle because it means two different indices point to the same next position
# When we find the entrance to the cycle, we've found our duplicate

# Example Walkthrough (Example 1: nums = [1,3,4,2,2])
# Goal: Find the duplicate (2).
# Array: [1,3,4,2,2] (length 5, values in [1,4]).
# Phase 1: Find Intersection:

# Start: tortoise = nums[0] = 1, hare = nums[0] = 1.
# Step 1:
# Tortoise: nums[1] = 3.
# Hare: nums[1] = 3, then nums[3] = 2.
# Step 2:
# Tortoise: nums[3] = 2.
# Hare: nums[2] = 4, then nums[4] = 2.
# Step 3:
# Tortoise: nums[2] = 4.
# Hare: nums[2] = 4, then nums[4] = 2.
# Step 4:
# Tortoise: nums[4] = 2.
# Hare: nums[2] = 4, then nums[4] = 2.
# Intersection: tortoise = hare = 2.
# Phase 2: Find Cycle Entrance:

# Reset: tortoise = nums[0] = 1, hare = 2.
# Step 1:
# Tortoise: nums[1] = 3.
# Hare: nums[2] = 4.
# Step 2:
# Tortoise: nums[3] = 2.
# Hare: nums[4] = 2.
# Meet at 2, so duplicate is 2.

