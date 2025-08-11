# https://leetcode.com/problems/two-sum/

# TC - O(N), SC - O(N)
def twoSum(nums, target):
    # Create a dictionary to store the complement of each number and its index
    prev_dict = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        diff = target - num

        # Check if the complement exists in our dictionary
        if diff in prev_dict:
            # If found, return both indices
            return [prev_dict[diff], i]

        # Otherwise, add the current number and its index to the dictionary
        prev_dict[num] = i

    return []


# Test cases
print(twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(twoSum([3, 2, 4], 6))       # Expected: [1, 2]
print(twoSum([3, 3], 6))          # Expected: [0, 1]