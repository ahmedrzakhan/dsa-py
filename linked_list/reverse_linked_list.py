# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC - O(N), SC - O(1)
def reverseList(head):
    prev, curr = None, head
    while curr:
        # Store the next node
        next_node = curr.next
        # Reverse the link
        curr.next = prev
        # Update prev to the current node for the next iteration
        prev = curr
        # Move curr to the next node in the original list
        curr = next_node
    return prev

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

head = create_list([1, 2, 3, 4, 5])
print("Original:", end=" ")
print_list(head)
print("Reversed:", end=" ")
print_list(reverseList(head))