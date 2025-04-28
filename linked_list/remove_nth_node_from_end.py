# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC - O(N), SC - O(1)
def removeNthFromEnd(head, n):
    # Create a dummy node to handle edge cases (like removing the head)
    dummy = ListNode(0)
    dummy.next = head

    # Initialize two pointers
    first = second = dummy

    # Advance first pointer by n+1 steps
    for _ in range(n + 1):
        if not first:
            return None
        first = first.next

    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    second.next = second.next.next

    # Return the new head
    return dummy.next

def create_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(head):
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals) if vals else "Empty")

# Example 1
head1 = create_list([1, 2, 3, 4, 5])
print("Original:")
print_list(head1)
result1 = removeNthFromEnd(head1, 2)
print("After removing 2nd node from end:")
print_list(result1)

# Example 2
head2 = create_list([1])
print("\nOriginal:")
print_list(head2)
result2 = removeNthFromEnd(head2, 1)
print("After removing 1st node from end:")
print_list(result2)

# Example 3
head3 = create_list([1, 2])
print("\nOriginal:")
print_list(head3)
result3 = removeNthFromEnd(head3, 1)
print("After removing 1st node from end:")
print_list(result3)

# The genius of this approach is in maintaining a precise gap between the two pointers.
# When the first pointer reaches the end, the second pointer will always be positioned
# exactly n nodes behind it.
