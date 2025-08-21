# https://leetcode.com/problems/task-scheduler/

from collections import Counter, deque
import heapq

# TC - O(NLogN), SC - O(N)
def leastInterval(tasks, n):
    # Count the frequency of each task using Counter
    count = Counter(tasks)  # e.g., for tasks=["A", "A", "B"], count = {'A': 2, 'B': 1}

    # Create a max heap by negating counts (since heapq is a min-heap)
    maxHeap = [-cnt for cnt in count.values()]  # e.g., [2, 1] becomes [-2, -1]
    heapq.heapify(maxHeap)  # Convert list into a heap for efficient max extraction

    time = 0  # Tracks the current time (or CPU cycles)
    q = deque()  # Queue to store tasks that are cooling down: [-count, idle_until_time]

    # Continue until both the heap and queue are empty
    while maxHeap or q:
        time += 1  # Increment time for each cycle

        # If no tasks are in the heap, jump to the earliest time a task is ready
        if not maxHeap:
            time = q[0][1]  # Set time to when the first task in queue is available
        else:
            # Pop the task with the highest remaining count (negated, so add 1)
            cnt = 1 + heapq.heappop(maxHeap)  # e.g., -2 becomes -1 (one task used)
            # If this task still has remaining executions, add it to the queue
            if cnt:
                q.append([cnt, time + n])  # Task waits until time + n (cooldown period)

        # Check if any task in the queue is ready to be executed (cooldown expired)
        if q and q[0][1] == time:
            # Move the task from queue back to heap (ready to execute again)
            heapq.heappush(maxHeap, q.popleft()[0])

    return time  # Return total time required to complete all tasks

tasks1 = ["A", "A", "A", "B", "B", "C"]
n1 = 1
print(leastInterval(tasks1, n1))  # Output: 8 (e.g., A->B->idle->A->B->idle->A->B)

# Example usage
# Example 1: Tasks need to be scheduled with a cooldown of 2
tasks2 = ["A", "A", "A", "B", "B", "B"]
n2 = 2
print(leastInterval(tasks2, n2))  # Output: 8 (e.g., A->B->idle->A->B->idle->A->B)

# Example 2: Tasks with a shorter cooldown of 1
tasks3 = ["A", "C", "A", "B", "D", "B"]
n3 = 1
print(leastInterval(tasks3, n3))  # Output: 6 (e.g., A->C->B->A->D->B)

# Example 3: Same tasks as Example 1 but with a longer cooldown of 3
tasks4 = ["A", "A", "A", "B", "B", "B"]
n4 = 3
print(leastInterval(tasks4, n4))  # Output: 10 (e.g., A->B->idle->idle->A->B->idle->idle->A->B)