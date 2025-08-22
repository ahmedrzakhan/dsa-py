# https://leetcode.com/problems/gas-station/

# TC - O(N), SC - O(1)
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]

        if total < 0:
            start = i + 1
            total = 0

    return start

# Test cases
# Test case 1
gas1 = [1, 2, 3, 4, 5]
cost1 = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas1, cost1))  # Expected: 3

# Test case 2
gas2 = [2, 3, 4]
cost2 = [3, 4, 3]
print(canCompleteCircuit(gas2, cost2))  # Expected: -1