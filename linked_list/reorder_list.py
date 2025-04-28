# https://leetcode.com/problems/reorder-list/description/

# TC - O(N), SC - O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return

    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    second_half = slow.next
    slow.next = None  # Break the list into two halves

    prev = None
    curr = second_half
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    second_half = prev  # Now second_half points to the head of the reversed second half

    # Step 3: Merge the two halves
    first_half = head
    while second_half:
        temp1 = first_half.next   # Save next node of first half
        temp2 = second_half.next  # Save next node of second half

        first_half.next = second_half  # Connect first half node to second half node
        second_half.next = temp1       # Connect second half node to next first half node

        first_half = temp1       # Move first half pointer forward
        second_half = temp2      # Move second half pointer forward

# Helper functions for testing
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
    print(" -> ".join(vals))

# Test cases
test1 = create_list([1, 2, 3, 4])
print("Original list 1:")
print_list(test1)
reorderList(test1)
print("Reordered list 1:")
print_list(test1)

test2 = create_list([1, 2, 3, 4, 5])
print("\nOriginal list 2:")
print_list(test2)
reorderList(test2)
print("Reordered list 2:")
print_list(test2)