# https://leetcode.com/problems/partition-labels

# TC - O(N), SC - O(1)
def partitionLabels(s):
    # Create a map of characters to their last occurrence index
    last_occurrence = {}
    for i, char in enumerate(s):
        last_occurrence[char] = i

    result = []
    start = 0
    end = 0

    # Iterate through the string
    for i, char in enumerate(s):
        # Update the end to the maximum last occurrence of characters seen
        end = max(end, last_occurrence[char])

        # If current index equals end, we've found a partition
        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result

# Test case 1
s1 = "ababcbacadefegdehijhklij"
print(f"Input: s = {s1}")
print(f"Output: {partitionLabels(s1)}")

# Test case 2
s2 = "eccbbbbdec"
print(f"Input: s = {s2}")
print(f"Output: {partitionLabels(s2)}")