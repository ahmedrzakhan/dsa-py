# https://leetcode.com/problems/3sum/description/

# TC -O(N^2), SC - O(1)
def threeSum(nums):
    # Sort the array first
    nums.sort()
    result = []
    N = len(nums)

    # Iterate through array, fixing the first number
    for i in range(N-2):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Use two pointers for the remaining two numbers
        L = i + 1
        R = N - 1

        while L < R:
            curr_sum = nums[i] + nums[L] + nums[R]

            if curr_sum == 0:
                # Found a valid triplet
                result.append([nums[i], nums[L], nums[R]])

                # Skip duplicates for Left
                while L < R and nums[L] == nums[L+1]:
                    L += 1
                # Skip duplicates for Right
                while L < R and nums[R] == nums[R-1]:
                    R -= 1

                L += 1
                R -= 1

            elif curr_sum < 0:
                L += 1
            else:
                R -= 1

    return result

# Test cases
test_cases = [
    # [-1,0,1,2,-1,-4],
    # [0,1,1],
    [0,0,0]
]

for nums in test_cases:
    print(f"Input: {nums}")
    print(f"Output: {threeSum(nums)}\n")