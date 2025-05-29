# https://leetcode.com/problems/partition-equal-subset-sum

# TC - O(N * target), SC - O(target)
def canPartition(A):
    # Check if the total sum of A is odd; if so, equal partitions are impossible
    if sum(A) % 2:
        return False

    # Initialize a set to store achievable subset sums
    DP = set()
    # Add 0 to represent the empty subset (sum of 0 is always possible)
    DP.add(0)
    # Calculate the target sum for each subset (half of total sum)
    target = sum(A) // 2

    # Iterate over A in reverse order (order doesn't affect correctness)
    for i in range(len(A) - 1, -1, -1):
        # Create a new set for the next iteration's achievable sums
        nextDP = set()
        # For each currently achievable sum t in dp
        for t in DP:
            # If adding the current number to t equals the target, we found a valid subset
            if (t + A[i]) == target:
                return True
            # Include the current number: add t + A[i] to possible sums
            nextDP.add(t + A[i])
            # Exclude the current number: keep t as a possible sum
            nextDP.add(t)
        # Update dp to the new set of achievable sums for the next iteration
        DP = nextDP

    # If no subset sums to target, return False
    return False

# Test cases
# Test case 1
nums1 = [1, 5, 11, 5]
print(canPartition(nums1))  # Should print: True

# Test case 2
nums2 = [1, 2, 3, 5]
print(canPartition(nums2))  # Should print: False