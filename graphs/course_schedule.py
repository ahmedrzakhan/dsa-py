# https://leetcode.com/problems/course-schedule

# TC - O(N+P), SC - O(N+P)
def canFinish(numCourses, prerequisites):
    # Create adjacency list for the graph
    adjList = [[] for _ in range(numCourses)]
    for pre in prerequisites:
        adjList[pre[1]].append(pre[0])

    # Track visited nodes and nodes currently being visited
    visited = set()    # Tracks visited courses
    visiting = set()   # Tracks courses currently being visited (for cycle detection)

    def dfs(course):
        if course in visiting:  # Cycle detected
            return False
        if course in visited:   # Already processed
            return True

        visiting.add(course)  # Mark as being visited
        for pre in adjList[course]:
            if not dfs(pre):
                return False  # Cycle detected in deeper recursion

        visiting.remove(course)  # Backtrack
        visited.add(course)      # Mark as processed
        return True

    # Check each course
    for i in range(numCourses):
        if not dfs(i):
            return False

    return True

# Test cases
# Test case 1
numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))  # Expected: True

# Test case 2
numCoursesF = 2
prerequisitesF = [[1, 0], [0, 1]]
print(canFinish(numCoursesF, prerequisitesF))  # Expected: False

# Test case 3
numOfCourses5 = 5
prerequisites5 = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
print(canFinish(numOfCourses5, prerequisites5))  # Expected: True

# Test case 4
numOfCourses3 = 3
prerequisites3 = [[1, 0], [2, 1], [0, 2]]
print(canFinish(numOfCourses3, prerequisites3))  # Expected: False