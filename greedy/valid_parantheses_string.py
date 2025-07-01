# https://leetcode.com/problems/valid-parenthesis-string

# TC - O(N), SC - O(1)
def checkValidString(s: str) -> bool:
    # Initialize variables to track the range of unmatched opening parentheses '('
    minOpen = 0  # Minimum possible unmatched '(' by treating '*' as ')' or empty
    maxOpen = 0  # Maximum possible unmatched '(' by treating '*' as '('

    # Process each character in the string
    for c in s:
        if c == "(":
            # An opening parenthesis increases both min and max unmatched '(' count
            minOpen += 1
            maxOpen += 1
        elif c == ")":
            # A closing parenthesis decreases both min and max unmatched '(' count
            minOpen -= 1
            maxOpen -= 1
        else:  # c == '*'
            # '*' can be '(', ')', or empty:
            # - As ')', decrease minOpen to minimize unmatched '('
            # - As '(', increase maxOpen to maximize unmatched '('
            minOpen -= 1
            maxOpen += 1

        # If maxOpen < 0, we have too many ')', even if all '*' are treated as '('
        # This means the string cannot be valid
        if maxOpen < 0:
            return False

        # If minOpen < 0, we've assumed too many '*' as ')', but '*' can be empty
        # Reset minOpen to 0 to reflect the minimum possible unmatched '('
        if minOpen < 0:
            minOpen = 0

    # String is valid if minOpen == 0, meaning we can balance all '(' in at least one way
    return minOpen == 0

# Test cases for local execution
test_cases = ["()", "(*)", "(*))"]
for s in test_cases:
    result = checkValidString(s)
    print(f"Input: s = \"{s}\"")
    print(f"Output: {result}\n")