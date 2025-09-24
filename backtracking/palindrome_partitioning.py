# https://leetcode.com/problems/palindrome-partitioning/

# TC - N*2^N, SC - O(N)
def partition(s):
    # Given a string s, partition s such that every substring of the partition is a palindrome.
    # Return all possible palindrome partitioning of s.
    # Args: s (str): Input string
    # Returns: List[List[str]]: All possible palindrome partitions
    def is_palindrome(string):
        return string == string[::-1]

    def backtrack(start, curr_set):
        # Backtracking function to find all palindrome partitions
        # Args: start (int): Starting index for current substring
        #     curr_set (List[str]): Current partition being built
        # Base case: if we've reached the end of string, add current partition to result
        if start == len(s):
            result.append(curr_set[:])  # Make a copy of current partition
            return

        # Try all possible substrings starting from 'start'
        for end in range(start + 1, len(s) + 1):
            sub_str = s[start:end]

            # If current substr is palindrome, add it to partition and recurse
            if is_palindrome(sub_str):
                curr_set.append(sub_str)
                backtrack(end, curr_set)
                curr_set.pop()  # Backtrack

    result = []
    backtrack(0, [])
    return result


def test_solution():
    """Test the solution with provided examples"""

    # Test case 1
    s1 = "aab"
    result1 = partition(s1)
    print(f"Input: '{s1}'")
    print(f"Output: {result1}")
    print(f"Expected: [['a','a','b'],['aa','b']]")
    print()

    # Test case 2
    s2 = "a"
    result2 = partition(s2)
    print(f"Input: '{s2}'")
    print(f"Output: {result2}")
    print(f"Expected: [['a']]")
    print()

    # Additional test case
    s3 = "racecar"
    result3 = partition(s3)
    print(f"Input: '{s3}'")
    print(f"Output: {result3}")
    print()


test_solution()
