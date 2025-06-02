# https://leetcode.com/problems/course-schedule-ii

# TC - O(V+E), SC - O(V+E)
def findOrder(numCourses, prerequisites):
    adjList = {}
    result = []
    visited = {}
    visiting = {}

    # Build adjacency list
    for pre in prerequisites:
        if pre[1] not in adjList:
            adjList[pre[1]] = []
        adjList[pre[1]].append(pre[0])

    for i in range(numCourses):
        if i not in visited:
            if not dfs(i, visiting, visited, adjList, result):
                return []  # Cycle detected or cannot finish all courses

    # Reverse the result to get the correct order
    for i in range(len(result) // 2):
        j = len(result) - 1 - i
        result[i], result[j] = result[j], result[i]

    return result

def dfs(course, visiting, visited, adjList, result):
    if course in visiting:  # Cycle detected
        return False
    if course in visited:  # Already processed
        return True

    visiting[course] = True
    for pre in adjList.get(course, []):
        if not dfs(pre, visiting, visited, adjList, result):
            return False  # Cycle detected in deeper recursion

    visiting.pop(course)  # Backtrack
    visited[course] = True  # Mark as processed
    result.append(course)  # Add course to result

    return True

numOfCourses5 = 5
prerequisites5 = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
print(findOrder(numOfCourses5, prerequisites5))  # Expected: e.g., [2, 4, 3, 1, 0]

numOfCourses3 = 3
prerequisites3 = [[1, 0], [2, 1], [0, 2]]
print(findOrder(numOfCourses3, prerequisites3))  # Expected: [] since there's a cycle