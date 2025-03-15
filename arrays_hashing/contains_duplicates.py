# https://leetcode.com/problems/contains-duplicate/

from typing import List

# TC - O(N), SC - O(N)
def containsDuplicate(nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


test1 = [1, 2, 3, 1]
test2 = [1, 2, 3, 4]
test3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(f"Test 1: {containsDuplicate(test1)}")  # Should print True
print(f"Test 2: {containsDuplicate(test2)}")  # Should print False
print(f"Test 3: {containsDuplicate(test3)}")  # Should print True

