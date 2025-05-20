# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_end_of_word

            if word[index] == '.':
                # Wildcard - try all possible characters
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                # Regular character - move to the specific child if exists
                if word[index] not in node.children:
                    return False
                return dfs(node.children[word[index]], index + 1)

        return dfs(self.root, 0)

# Example usage
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

# Test cases
test_cases = ["pad", "bad", ".ad", "b.."]
for test in test_cases:
    print(f"Search '{test}': {wordDictionary.search(test)}")