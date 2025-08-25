# https://neetcode.io/problems/valid-tree

# TC - O(V+E), SC - O(V+E)
def validTree(n: int, edges: list[list[int]]) -> bool:
    # A valid tree must have exactly n-1 edges and be fully connected (no cycles)
    if len(edges) != n - 1:
        return False

    # Build adjacency list
    adjList = [[] for _ in range(n)]
    for src, dst in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)

    # Use DFS to detect cycles and check connectivity
    visited = {}

    def dfs(node: int, parent: int) -> bool:
        visited[node] = True
        for neighbor in adjList[node]:
            # Skip the parent node to avoid false cycle detection
            if neighbor == parent:
                continue
            # If neighbor is already visited, we found a cycle
            if neighbor in visited:
                return False
            # Recursively check for cycles from the neighbor
            if not dfs(neighbor, node):
                return False
        return True

    # Start DFS from node 0
    if not dfs(0, -1):
        return False

    # Check if all nodes are connected (visited)
    return len(visited) == n

# Test cases
# Test case 1: Valid tree
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print("Test 1:", validTree(n, edges))  # Expected: True

# Test case 2: Invalid tree (contains cycle)
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print("Test 2:", validTree(n, edges))  # Expected: False

# Test case 3: Single node
n = 1
edges = []
print("Test 3:", validTree(n, edges))  # Expected: True

# Test case 4: Disconnected graph
n = 4
edges = [[0, 1], [2, 3]]
print("Test 4:", validTree(n, edges))  # Expected: False


# NOTE: If it has fewer than n-1 edges, it cannot be connected
# If it has more than n-1 edges, it must contain at least one cycle
# If it has exactly n-1 edges, it can be a tree (but you still need to verify connectivity)

