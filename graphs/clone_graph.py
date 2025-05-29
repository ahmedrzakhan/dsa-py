# Definition for a Node (matching Go's Node struct)
class Node:
    def __init__(self, Val=0, Neighbors=None):
        self.val = Val
        self.neighbors = Neighbors if Neighbors is not None else []

# TC - O(N+E), SC - O(N)
def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None

    visited = {}  # Map original node to its clone

    def dfsClone(node):
        if node in visited:
            return visited[node]

        newNode = Node(node.val)
        visited[node] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(dfsClone(neighbor))
        return newNode

    return dfsClone(node)

# Test function matching Go's mainCloneGraph
def mainCloneGraph():
    # Example 1: Graph with nodes 1->(2,4), 2->(1,3), 3->(2,4), 4->(1,3)
    node1 = Node(Val=1)
    node2 = Node(Val=2)
    node3 = Node(Val=3)
    node4 = Node(Val=4)
    node1.Neighbors = [node2, node4]
    node2.Neighbors = [node1, node3]
    node3.Neighbors = [node2, node4]
    node4.Neighbors = [node1, node3]

    clonedGraph = cloneGraph(node1)
    print(f"Cloned Node Value: {clonedGraph.Val}")
    for neighbor in clonedGraph.Neighbors:
        print(f"Neighbor: {neighbor.Val}")

    # Example 2: Single node with no neighbors
    nodeWithNoNeighbors = Node(Val=1)
    clonedEmptyNodeGraph = cloneGraph(nodeWithNoNeighbors)
    print(f"Cloned Node Value (Empty Node): {clonedEmptyNodeGraph.Val}")
    print(f"Number of Neighbors (should be 0): {len(clonedEmptyNodeGraph.Neighbors)}")

    # Example 3: Empty graph
    emptyGraph = cloneGraph(None)
    if emptyGraph is None:
        print("Cloned empty graph successfully. Result is None, as expected.")
    else:
        print("Error: Expected None for empty graph clone")

if __name__ == "__main__":
    mainCloneGraph()