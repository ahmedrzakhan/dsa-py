# https://leetcode.com/problems/contains-duplicate/

from typing import List

# TC - O(N), SC - O(N)
def containsDuplicate(A: List[int]) -> bool:
        # Convert the list to a set (which removes duplicates) and compare lengths
        # If the original list length is not equal to the set length,
        # it means some elements were duplicates that got removed
        return len(A) != len(set(A))


test1 = [1, 2, 3, 1]
test2 = [1, 2, 3, 4]
test3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(f"Test 1: {containsDuplicate(test1)}")  # Should print True
print(f"Test 2: {containsDuplicate(test2)}")  # Should print False
print(f"Test 3: {containsDuplicate(test3)}")  # Should print True

