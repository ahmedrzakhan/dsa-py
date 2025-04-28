# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

# TC - O(N), SC - O(1)
def copyRandomList(head):
    if not head:
        return None

    # Step 1: Create a new node for each existing node and insert it between the original nodes
    curr = head
    while curr:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next

    # Step 2: Set random pointers for the new nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the original and copied lists
    curr = head
    new_head = head.next
    new_curr = new_head

    while curr:
        curr.next = curr.next.next if curr.next else None
        if new_curr.next:
            new_curr.next = new_curr.next.next
        curr = curr.next
        new_curr = new_curr.next

    return new_head

# Helper functions to create and print a list with random pointers
def create_random_list(values_and_random_indices):
    if not values_and_random_indices:
        return None

    # First pass: Create all nodes
    nodes = []
    for val, _ in values_and_random_indices:
        nodes.append(Node(val))

    # Second pass: Link next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Third pass: Link random pointers
    for i, (_, random_index) in enumerate(values_and_random_indices):
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0] if nodes else None

def print_random_list(head):
    result = []
    node_to_index = {}

    # First pass: Map nodes to indices
    index = 0
    curr = head
    while curr:
        node_to_index[curr] = index
        index += 1
        curr = curr.next

    # Second pass: Print values and random indices
    curr = head
    while curr:
        random_index = node_to_index.get(curr.random, None) if curr.random else None
        result.append([curr.val, random_index])
        curr = curr.next

    print(result)

# Test cases
def test_copy_random_list():
    print("Test Case 1:")
    head1 = create_random_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    print("Original list:")
    print_random_list(head1)
    copied1 = copyRandomList(head1)
    print("Copied list:")
    print_random_list(copied1)

    print("\nTest Case 2:")
    head2 = create_random_list([[1, 1], [2, 1]])
    print("Original list:")
    print_random_list(head2)
    copied2 = copyRandomList(head2)
    print("Copied list:")
    print_random_list(copied2)

    print("\nTest Case 3:")
    head3 = create_random_list([[3, None], [3, 0], [3, None]])
    print("Original list:")
    print_random_list(head3)
    copied3 = copyRandomList(head3)
    print("Copied list:")
    print_random_list(copied3)

# Run tests
test_copy_random_list()