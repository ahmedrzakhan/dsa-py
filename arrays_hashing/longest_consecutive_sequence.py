# https://leetcode.com/problems/longest-consecutive-sequence/description/

# TC - O(N), SC - O(N)
def longestConsecutive(nums):
    # Convert array to set for O(1) lookup, also getting rid of all duplicates
    num_set = set(nums)
    max_length = 0

    # Iterate through each number
    for num in num_set:
        # Only start checking sequences from the smallest number in the sequence
        if num - 1 not in num_set:
            curr_num = num
            curr_length = 1

            # Keep checking consecutive numbers
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_length += 1

            # Update max_length streak if current streak is longer
            max_length = max(max_length, curr_length)

    return max_length

# Test cases
print(longestConsecutive([100,4,200,1,3,2]))  # Output: 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
print(longestConsecutive([1,0,1,2]))  # Output: 3