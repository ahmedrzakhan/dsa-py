# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Insert a word into the trie.
        # Args: word: The word to insert into the trie
        # Time Complexity: O(m) where m is the length of the word
        # Space Complexity: O(m) in worst case when no prefixes exist
        curr = self.root

        # Traverse through each character in the word
        for ch in word:
            # If character doesn't exist as a child, create a new node
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            # Move to the child node for this character
            curr = curr.children[ch]

        # Mark the final node as end of a complete word
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            # Depth-first search helper function to match word pattern starting from position j
            # Args: j: Current position in the word being searched
            #     root: Current trie node to search from
            curr = root

            # Iterate through remaining characters in the word starting from position j
            for i in range(j, len(word)):
                ch = word[i]

                # Handle wildcard character '.'
                if ch == ".":
                    # Try matching '.' with any available child node
                    for child in curr.children.values():
                        # Recursively search from next position with each child
                        if dfs(i + 1, child):
                            return True
                    # If no child leads to a successful match, return False
                    return False
                else:
                    # Handle regular character
                    # Check if current character exists as a child
                    if ch not in curr.children:
                        return False
                    # Move to the child node corresponding to current character
                    curr = curr.children[ch]

            # After processing all characters, check if current node marks end of a word
            return curr.is_end_of_word

        # Start DFS from position 0 and root of the trie
        return dfs(0, self.root)

# Example usage
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

# Test cases
test_cases = ["pad", "bad", ".ad", "b..", "b.d"]
for test in test_cases:
    print(f"Search '{test}': {wordDictionary.search(test)}")