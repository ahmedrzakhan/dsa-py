# https://neetcode.io/problems/valid-tree

# TC - O(V+E), SC - O(V+E)
def validTree(n: int, edges: list[list[int]]) -> bool:
    # Quick check: valid tree must have exactly n-1 edges
    if len(edges) != n - 1:
        return False

    # If we have n-1 edges and the graph is connected, it's a tree
    # Build adjacency list
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # DFS to check connectivity
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Start from any node (0) and see if we can reach all nodes
    dfs(0)
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

