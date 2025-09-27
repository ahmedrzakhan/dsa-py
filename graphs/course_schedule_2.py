# https://leetcode.com/problems/course-schedule-ii

# TC - O(V+E), SC - O(V+E)
def findOrder(numCourses, prerequisites):
    # Create adjacency list for the graph
    adjList = [[] for _ in range(numCourses)]
    for pre in prerequisites:
        adjList[pre[1]].append(pre[0])

    # Track visited nodes and nodes currently being visited
    visited = set() # Tracks visited courses
    visiting = set() # Tracks courses currently being visited (for cycle detection)
    result = []

    def dfs(course):
        if course in visiting: # Cycle detected
            return False
        if course in visited: # Already processed
            return True

        visiting.add(course) # Mark as being visited
        for pre in adjList[course]:
            if not dfs(pre):
                return False  # Cycle detected in deeper recursion

        visiting.remove(course)  # Backtrack
        visited.add(course)  # Mark as processed
        result.append(course)
        return True

    # Check each course
    for i in range(numCourses):
        if i not in visited and not dfs(i):
            return []

    return result[::-1]

# Test cases
# Test case 1
numOfCourses5 = 5
prerequisites5 = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
print(findOrder(numOfCourses5, prerequisites5))  # Expected: e.g., [2, 4, 3, 1, 0]

# Test case 2
numOfCourses3 = 3
prerequisites3 = [[1, 0], [2, 1], [0, 2]]
print(findOrder(numOfCourses3, prerequisites3))  # Expected: [] since there's a cycle