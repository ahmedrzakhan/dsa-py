# https://neetcode.io/problems/count-connected-components

# TC - O(V+E), SC - O(V)
def countComponents(n, edges):
    # Build adjacency list
    adj_list = [[] for _ in range(n)]
    for src, dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1

    return components

# Test cases
edges1 = [[0, 1], [0, 2]]
print(f"Test 1: n = 3, edges = {edges1}")
print(f"Output: {countComponents(3, edges1)}")  # Expected: 1

edges2 = [[0, 1], [1, 2], [2, 3], [4, 5]]
print(f"Test 2: n = 6, edges = {edges2}")
print(f"Output: {countComponents(6, edges2)}")  # Expected: 2