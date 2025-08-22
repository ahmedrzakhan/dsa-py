# https://leetcode.com/problems/word-search/

# TC - O(R*C*4^L), SC - O(N)
def word_search(M, word):
    # Find if word exists in the board using backtracking.
    # Args:
    #     board: List[List[str]] - m x n grid of characters
    #     word: str - word to search for
    # Returns:
    #     bool - True if word exists in grid, False otherwise
    if not M or not M[0] or not word:
        return False

    ROWS, COLS = len(M), len(M[0])

    def backtrack(R, C, index):
        # Base case: found the complete word
        if index == len(word):
            return True

        # Check bounds and character match
        if (R < 0 or R >= ROWS or C < 0 or C >= COLS or
            M[R][C] != word[index] or M[R][C] == '#'):
            return False

        # Mark current cell as visited
        temp = M[R][C]
        M[R][C] = '#'

        # Explore all 4 directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for next_row, next_col in directions:
            if backtrack(R + next_row, C + next_col, index + 1):
                return True

        # Restore the cell (backtrack)
        M[R][C] = temp

        return False

    # Try starting from each cell in the board
    for i in range(ROWS):
        for j in range(COLS):
            if backtrack(i, j, 0):
                return True

    return False


def test_word_search():
    """Test the word search solution with provided examples."""

    # Test Case 1
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    result1 = word_search(board1, word1)
    print(f"Test 1: board = {board1}, word = '{word1}'")
    print(f"Expected: True, Got: {result1}")
    print(f"✓ Passed\n" if result1 == True else f"✗ Failed\n")

    # Test Case 2
    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word2 = "SEE"
    result2 = word_search(board2, word2)
    print(f"Test 2: board = {board2}, word = '{word2}'")
    print(f"Expected: True, Got: {result2}")
    print(f"✓ Passed\n" if result2 == True else f"✗ Failed\n")

    # Test Case 3
    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word3 = "ABCB"
    result3 = word_search(board3, word3)
    print(f"Test 3: board = {board3}, word = '{word3}'")
    print(f"Expected: False, Got: {result3}")
    print(f"✓ Passed\n" if result3 == False else f"✗ Failed\n")

    # Additional test cases
    # Test Case 4: Single character
    board4 = [["A"]]
    word4 = "A"
    result4 = word_search(board4, word4)
    print(f"Test 4: board = {board4}, word = '{word4}'")
    print(f"Expected: True, Got: {result4}")
    print(f"✓ Passed\n" if result4 == True else f"✗ Failed\n")

    # Test Case 5: Word longer than available cells
    board5 = [["A","B"],["C","D"]]
    word5 = "ABCDEF"
    result5 = word_search(board5, word5)
    print(f"Test 5: board = {board5}, word = '{word5}'")
    print(f"Expected: False, Got: {result5}")
    print(f"✓ Passed\n" if result5 == False else f"✗ Failed\n")


print("Word Search Problem Solution\n" + "="*40)
test_word_search()

# Interactive testing
print("\nInteractive Testing:")
print("You can test with custom inputs:")
print("board = [['A','B'],['C','D']]")
print("word = 'ABDC'")
print("result = word_search(board, word)")
print("print(result)")