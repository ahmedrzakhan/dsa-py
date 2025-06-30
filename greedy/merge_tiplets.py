# https://leetcode.com/problems/merge-triplets-to-form-target-triplet

# TC - O(N), SC - O(1)
def can_form_target(triplets, target):
    x, y, z = target

    # Track if we can achieve each target value
    can_achieve_x = False
    can_achieve_y = False
    can_achieve_z = False

    for a, b, c in triplets:
        # Skip if any value exceeds the target in that position
        if a > x or b > y or c > z:
            continue

        # Check if this triplet can contribute to achieving target values
        if a == x:
            can_achieve_x = True
        if b == y:
            can_achieve_y = True
        if c == z:
            can_achieve_z = True

    # Return true only if all target values can be achieved
    return can_achieve_x and can_achieve_y and can_achieve_z

# Test case 1
triplets1 = [[2,5,3],[1,8,4],[1,7,5]]
target1 = [2,7,5]
print(can_form_target(triplets1, target1))  # Output: True

# Test case 2
triplets2 = [[3,4,5],[4,5,6]]
target2 = [3,2,5]
print(can_form_target(triplets2, target2))  # Output: False

# Test case 3
triplets3 = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target3 = [5,5,5]
print(can_form_target(triplets3, target3))  # Output: True