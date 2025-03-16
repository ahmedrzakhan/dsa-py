# https://leetcode.com/problems/two-sum/

# TC - O(N), SC - O(N)
def twoSum(nums, target):
    # Create a dictionary to store the complement of each number and its index
    num_hash = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement exists in our dictionary
        if complement in num_hash:
            # If found, return both indices
            return [num_hash[complement], i]

        # Otherwise, add the current number and its index to the dictionary
        num_hash[num] = i

    return []


# Test cases
print(twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(twoSum([3, 2, 4], 6))       # Expected: [1, 2]
print(twoSum([3, 3], 6))          # Expected: [0, 1]