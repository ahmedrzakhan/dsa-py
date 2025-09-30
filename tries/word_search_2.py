class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""  # Store the complete word at leaf nodes

    def insert(self, word):
        """Insert a word into the Trie."""
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = word


def findWords(M, words):
    # Find all words from the words list that exist in the board.
    # Args: board: List[List[str]] - m x n grid of characters
    #     words: List[str] - list of words to search for
    # Returns: List[str] - all words found in the board

    # Time Complexity: O(M*N*4^L) where M,N are board dimensions, L is max word length
    # Space Complexity: O(A*L) where A is alphabet size, L is max word length
    ROWS, COLS = len(M), len(M[0])
    result = []

    if ROWS == 0 or COLS == 0:
        return result

    def dfs(R, C, curr, result):
        # Perform DFS to find words starting from position (R, C).
        # Args: R, C: current row and column position
        #     ROWS, COLS: board dimensions
        #     curr: current Trie node
        #     result: list to store found words
        #     board: the game board
        # Check boundaries
        if R < 0 or R >= ROWS or C < 0 or C >= COLS:
            return

        temp = M[R][C]

        # Check if character exists in Trie or if cell is already visited
        if temp not in curr.children or temp == '#':
            return

        # Move to next Trie node
        next_node = curr.children[temp]

        # Check if a word is found
        if next_node.word != "":
            result.append(next_node.word)
            next_node.word = ""  # Avoid duplicates

        # Mark current cell as visited
        M[R][C] = '#'

        # Explore all 4 directions
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for direction in directions:
            next_row, next_col = R + direction[0], C + direction[1]
            dfs(next_row, next_col, next_node)

        # Restore the cell value (backtrack)
        M[R][C] = temp

    # Build Trie from all words
    curr = TrieNode()
    for word in words:
        curr.insert(word)

    # Try DFS from each cell
    for R in range(ROWS):
        for C in range(COLS):
            dfs(R, C, curr, result)

    return result



def new_trie_node():
    """Factory function to create a new TrieNode (Go-style naming)."""
    return TrieNode()


# Test the solution
def test_word_search():

    # Test Case 1
    board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words1 = ["oath","pea","eat","rain"]
    result1 = findWords(board1, words1)
    print(f"Test 1 - Input: {words1}")
    print(f"Output: {sorted(result1)}")
    print(f"Expected: ['eat', 'oath']")
    print()

    # Test Case 2
    board2 = [["a","b"],["c","d"]]
    words2 = ["abcb"]
    result2 = findWords(board2, words2)
    print(f"Test 2 - Input: {words2}")
    print(f"Output: {result2}")
    print(f"Expected: []")
    print()

    # Test Case 3 - Additional test
    board3 = [["a","b","c"],["a","e","d"],["a","f","g"]]
    words3 = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "afg", "ade"]
    result3 = findWords(board3, words3)
    print(f"Test 3 - Input: {words3}")
    print(f"Output: {sorted(result3)}")

if __name__ == "__main__":
    test_word_search()