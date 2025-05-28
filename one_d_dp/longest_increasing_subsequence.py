# https://leetcode.com/problems/longest-increasing-subsequence

# TC - O(NLogN), SC - O(N)
def lengthOfLIS(nums):
    # tails[i] stores the smallest value that ends an increasing subsequence of length i+1
    tails = []

    for num in nums:
        # Binary search to find the position to insert num
        L, R = 0, len(tails)
        while L < R:
            mid = (L + R) // 2
            if tails[mid] < num:
                L = mid + 1
            else:
                R = mid
        # If we're at the end, append the number
        if L == len(tails):
            tails.append(num)
        # Otherwise, replace the number at position left
        else:
            tails[L] = num

    return len(tails)

# Test cases
test_cases = [
    [10,9,2,5,3,7,101,18],
    [0,1,0,3,2,3],
    [7,7,7,7,7,7,7]
]

for nums in test_cases:
    print(f"Input: {nums}")
    print(f"Output: {lengthOfLIS(nums)}\n")