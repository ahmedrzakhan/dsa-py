# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

# TC - O(N*LogK), SC - OLogK
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        merged_lists = []

        # Merge pairs of lists
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged_lists.append(mergeTwoLists(l1, l2))

        lists = merged_lists

    return lists[0]

def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # Append remaining nodes
    curr.next = l1 or l2

    return dummy.next

# Helper functions for testing
def create_linked_list(arr):
    """Create a linked list from an array"""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    """Convert linked list to array for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the solution
def test_merge_k_lists():

    # Test case 1: [[1,4,5],[1,3,4],[2,6]]
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result = mergeKLists(lists)
    print("Test 1:", linked_list_to_array(result))  # Expected: [1,1,2,3,4,4,5,6]

    # Test case 2: []
    result = mergeKLists([])
    print("Test 2:", linked_list_to_array(result))  # Expected: []

    # Test case 3: [[]]
    result = mergeKLists([None])
    print("Test 3:", linked_list_to_array(result))  # Expected: []

    # Test case 4: Single list
    result = mergeKLists([create_linked_list([1, 2, 3])])
    print("Test 4:", linked_list_to_array(result))  # Expected: [1,2,3]


test_merge_k_lists()