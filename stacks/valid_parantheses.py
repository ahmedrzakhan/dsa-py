# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    # Create a stack to store opening brackets
    stack = []

    # Dictionary to map closing brackets to their corresponding opening brackets
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Iterate through each character in the string
    for ch in s:
        # If it's an opening bracket, push to stack
        if ch in '({[':
            stack.append(ch)
        # If it's a closing bracket
        elif ch in ')}]':
            # If stack is empty or top of stack doesn't match corresponding opening bracket
            if not stack or stack.pop() != brackets[ch]:
                return False

    # String is valid only if stack is empty (all brackets matched)
    return len(stack) == 0

# Test cases
test_cases = ["()", "()[]{}", "(]", "([])"]
for test in test_cases:
    print(f"Input: {test}, Output: {isValid(test)}")