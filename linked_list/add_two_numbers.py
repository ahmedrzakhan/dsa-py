# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper functions to create and display linked lists
def createLinkedList(arr):
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedListToArray(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# TC - O(Max(N, M)), SC - O(Max(N, M))
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Create a dummy head node to simplify the code
    dummy_head = ListNode(0)
    curr = dummy_head

    # Initialize carry to 0
    carry = 0

    # Traverse both lists simultaneously
    while l1 or l2 or carry:
        # Get values from the curr nodes (or 0 if the list ended)
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        # Calculate the sum and carry
        total = x + y + carry
        carry = total // 10
        digit = total % 10

        # Create a new node with the calculated digit
        curr.next = ListNode(digit)
        curr = curr.next

        # Move to the next nodes in the lists if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Return the result linked list (without the dummy head)
    return dummy_head.next

# Test cases
def runTestCase(l1_arr, l2_arr):
    l1 = createLinkedList(l1_arr)
    l2 = createLinkedList(l2_arr)
    result = addTwoNumbers(l1, l2)
    return linkedListToArray(result)

# Example 1
print("Example 1:")
print("Input: l1 = [2,4,3], l2 = [5,6,4]")
output1 = runTestCase([2,4,3], [5,6,4])
print(f"Output: {output1}")
print("Expected: [7,0,8]")

# Example 2
print("\nExample 2:")
print("Input: l1 = [0], l2 = [0]")
output2 = runTestCase([0], [0])
print(f"Output: {output2}")
print("Expected: [0]")

# Example 3
print("\nExample 3:")
print("Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]")
output3 = runTestCase([9,9,9,9,9,9,9], [9,9,9,9])
print(f"Output: {output3}")
print("Expected: [8,9,9,9,0,0,0,1]")