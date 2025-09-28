# https://leetcode.com/problems/redundant-connection/

# TC - O(N), SC - O(N)
def findRedundantConnection(edges):
    # Initialize parent array for Union-Find
    N = len(edges)
    parent = [i for i in range(N+1)]
    def find(x):
        # Find the root of x with path compression
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        # Union by setting parent of x's root to y's root
        parent[find(x)] = find(y)

    # Initialize variable to store the redundant edge
    redundant = []

    # Process each edge
    for u, v in edges:
        # If nodes u and v have the same root, this edge creates a cycle
        if find(u) == find(v):
            redundant = [u, v]  # Update redundant edge, keeping the last occurrence
        else:
            # Otherwise, union the two nodes
            union(u, v)

    return redundant

# Test cases
# Test case 1
edges1 = [[1,2],[1,3],[2,3]]
print("Test 1:", findRedundantConnection(edges1))  # Expected: [2,3]

# Test case 2
edges2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print("Test 2:", findRedundantConnection(edges2))  # Expected: [1,4]
