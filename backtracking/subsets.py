# https://leetcode.com/problems/subsets/description/

# TC - O(2^N), SC - O(N)
def subsets(A):
    result = []

    def backtrack(start, curr_set):
        # Add current subset to result
        result.append(curr_set[:])

        # Explore all possible elements from start index
        for i in range(start, len(A)):
            # Include current element
            curr_set.append(A[i])
            # Recurse with next index
            backtrack(i + 1, curr_set)
            # Backtrack by removing the last element
            curr_set.pop()

    backtrack(0, [])
    return result

# Test cases
test1 = [1, 2, 3]
test2 = [0]
print(subsets(test1))  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2], [1, 2, 3]]
print(subsets(test2))  # Output: [[], [0]]