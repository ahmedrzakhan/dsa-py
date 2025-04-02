# https://leetcode.com/problems/min-stack/description/

# TC - O(N), SC - O(1) for all operations
class MinStack:
    def __init__(self):
        # Initialize two stacks: one for values and one for tracking minimums
        self.stack = []         # Main stack for all values
        self.min_stack = []     # Stack to keep track of minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or new value is less than or equal to current min,
        # add it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If the popped value is the current minimum,
        # remove it from min_stack as well
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Test the implementation
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # Output: -3
    minStack.pop()
    print(minStack.top())     # Output: 0
    print(minStack.getMin())  # Output: -2