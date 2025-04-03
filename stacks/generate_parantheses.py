# TC - O(4^N/sqrt(n)), SC - O(N)
def generateParenthesis(n):
    def backtrack(open_count, close_count, curr, result):
        # If current string length equals 2*n, we've used all parentheses
        if len(curr) == 2 * n:
            result.append(curr)
            return

        # We can add an opening parenthesis if we haven't used all n opening ones
        if open_count < n:
            backtrack(open_count + 1, close_count, curr + "(", result)

        # We can add a closing parenthesis if we have more open than closed
        if close_count < open_count:
            backtrack(open_count, close_count + 1, curr + ")", result)

    result = []
    backtrack(0, 0, "", result)
    return result

# Test cases
print(generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(1))  # ["()"]



# Time Complexity: O(4^n / √n)
# Simple Explanation:

# The goal is to generate all possible valid combinations of n pairs of parentheses.
# The number of valid combinations is a known mathematical count called the nth Catalan number.
# For example:
# n = 1 → 1 combination ("()")
# n = 2 → 2 combinations ("()()", "(())")
# n = 3 → 5 combinations ("((()))", "(()())", "(())()", "()(())", "()()()")
# This number grows fast, but not as fast as 2^(2n) (all possible strings of length 2n).
# Mathematicians have figured out it’s roughly 4^n divided by √n (with some constants we ignore in big-O).
# Why 4^n? Think of it as exploring a branching tree where we make choices at 2n positions, but the √n reduces it because only some paths are valid.
# So, TC is O(4^n / √n) because that’s how many combinations we generate, and we spend a little time building each one.
# Quick Interview Version:
# "The time complexity is O(4^n / √n) because we’re generating all valid parentheses combinations, which is the nth Catalan number. It grows like 4^n but gets reduced by √n due to the rules of valid parentheses. We just count the outputs we make."