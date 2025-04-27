# https://leetcode.com/problems/linked-list-cycle/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC - O(N), SC - O(1)
def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    # Initialize two pointers - slow and fast
    slow = head
    fast = head

    # Move slow one step and fast two steps at a time
    while fast and fast.next:
        slow = slow.next        # Move slow pointer by 1 step
        fast = fast.next.next   # Move fast pointer by 2 steps

    # If they meet, there's a cycle
        if slow == fast:
            return True

    # If fast reaches the end (null), there's no cycle
    return False


def create_cyclic_list(vals, pos):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    nodes = [head]

    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
        nodes.append(curr)

    # Create cycle if pos is valid
    if pos >= 0 and pos < len(nodes):
        curr.next = nodes[pos]

    return head

# Test cases
list1 = create_cyclic_list([3, 2, 0, -4], 1)  # Should have cycle
list2 = create_cyclic_list([1, 2], 0)        # Should have cycle
list3 = create_cyclic_list([1], -1)          # No cycle

print(f"Test 1: {hasCycle(list1)}")  # Expected: True
print(f"Test 2: {hasCycle(list2)}")  # Expected: True
print(f"Test 3: {hasCycle(list3)}")  # Expected: False