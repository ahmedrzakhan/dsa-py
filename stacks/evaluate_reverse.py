# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# TC - O(N), SC - O(N)
def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            # Pop the two operands (second operand first due to stack order)
            b = stack.pop()
            a = stack.pop()

            # Perform the operation
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # division
                # Handle division with truncation toward zero
                # Python's // operator truncates toward negative infinity
                # We need to handle negative numbers specially
                stack.append(int(a / b))
        else:
            # If token is a number, convert to integer and push to stack
            stack.append(int(token))

    return stack[0]

# Test cases
test1 = ["2","1","+","3","*"]
print(evalRPN(test1))  # Output: 9

test2 = ["4","13","5","/","+"]
print(evalRPN(test2))  # Output: 6

test3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(test3))  # Output: 22