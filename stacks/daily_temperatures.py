# https://leetcode.com/problems/daily-temperatures/description/

# TC - O(N), SC - O(N)
def dailyTemperatures(temperatures):
  # Initialize result array with zeros, same length as input temperatures
    res = [0] * len(temperatures)

    # Initialize empty stack to store pairs of [temperature, index]
    stack = []  # pair: [temp, index]

    # Iterate through temperatures array with index and value using enumerate
    for i, t in enumerate(temperatures):
        # While stack is not empty AND current temperature is warmer than
        # the temperature at the top of stack
        while stack and t > stack[-1][0]:
            # Pop the last pair from stack and unpack into temperature and index
            stackT, stackIdx = stack.pop()
            # Calculate days difference between current index and popped index
            # Store result in the corresponding position in res array
            res[stackIdx] = i - stackIdx
        # Add current temperature and index as a tuple to the stack
        stack.append((t, i))

    # Return the result array
    # Any indices remaining in stack will have 0 in res (no warmer day found)
    return res

# Test cases
test1 = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(test1))  # [1,1,4,2,1,1,0,0]

test2 = [30,40,50,60]
print(dailyTemperatures(test2))  # [1,1,1,0]

test3 = [30,60,90]
print(dailyTemperatures(test3))  # [1,1,0]


# Key Concepts:

# Monotonic Stack: The stack maintains temperatures in a decreasing order.
# When we find a warmer day, we can resolve waiting periods for colder days.