# https://leetcode.com/problems/lru-cache/description/

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # map key to node
        self.size = 0
        self.capacity = capacity

        # Use dummy head and tail nodes
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Add node right after head
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    # Remove an existing node from the linked list
    def _remove_node(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    # Move a node to the head (mark as most recently used)
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    # Pop the least recently used node (the one before tail)
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1

        # Move the accessed node to the head
        self._move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            # Create a new node
            newNode = DLinkedNode(key, value)

            # Add to the cache
            self.cache[key] = newNode

            # Add to the doubly linked list
            self._add_node(newNode)

            self.size += 1

            # If over capacity, remove the LRU item
            if self.size > self.capacity:
                # Remove the tail node
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # Update the value and move to head
            node.value = value
            self._move_to_head(node)

# Test code based on the example
def test_lru_cache():
    print("Testing LRU Cache implementation...")

    # Test case from problem statement
    operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    params = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expected = [None, None, None, 1, None, -1, None, -1, 3, 4]

    cache = None
    results = []

    for i in range(len(operations)):
        op = operations[i]
        param = params[i]

        if op == "LRUCache":
            cache = LRUCache(param[0])
            results.append(None)
        elif op == "put":
            results.append(cache.put(param[0], param[1]))
        elif op == "get":
            results.append(cache.get(param[0]))

    # Print results
    print("Expected:", expected)
    print("Actual:  ", results)

    # Check if results match expected
    if results == expected:
        print("✅ All tests passed!")
    else:
        print("❌ Tests failed!")

test_lru_cache()