# https://neetcode.io/problems/count-connected-components

# TC - O(V+E), SC - O(V)
def countComponents(n, edges):
    # Initialize parent and rank arrays
    parent = list(range(n))
    rank = [1] * n  # Add rank array, initialized to 1

    def find(x):
        # Find with path compression
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        # Union by rank
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] > rank[py]:
            px, py = py, px  # Swap so py has higher rank
        parent[px] = py  # Always attach px (smaller) to py (larger)
        rank[py] += rank[px]  # Update the larger tree's rank

    # Process edges
    for a, b in edges:
        union(a, b)

    # Count unique roots (components)
    components = set()
    for i in range(n):
        components.add(find(i))

    return len(components)

# Test cases
edges1 = [[0, 1], [0, 2]]
print(f"Test 1: n = 3, edges = {edges1}")
print(f"Output: {countComponents(3, edges1)}")  # Expected: 1

edges2 = [[0, 1], [1, 2], [2, 3], [4, 5]]
print(f"Test 2: n = 6, edges = {edges2}")
print(f"Output: {countComponents(6, edges2)}")  # Expected: 2