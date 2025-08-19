# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    # Node class for the Trie data structure.
    # Each node represents a character in the trie and contains references to its children.
    def __init__(self):
        # Dictionary to store child nodes, where key is character and value is TrieNode
        self.children = {}
        # Boolean flag to mark if this node represents the end of a complete word
        self.is_end_of_word = False

class Trie:
    # Trie (Prefix Tree) data structure implementation. Supports efficient insertion, search,
    # and prefix matching operations.
    def __init__(self):
        # Initialize the trie with an empty root node.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
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
        # Search for a complete word in the trie.
        # Args: word: The word to search for
        # Returns: True if the word exists as a complete word in the trie, False otherwise
        # Time Complexity: O(m) where m is the length of the word
        # Space Complexity: O(1)
        curr = self.root

        # Traverse through each character in the word
        for ch in word:
            # If character doesn't exist in current node's children, word not found
            if ch not in curr.children:
                return False
            # Move to the child node for this character
            curr = curr.children[ch]

        # Return True only if we've reached a node that marks end of a word
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Check if any word in the trie starts with the given prefix.
        # Args: prefix to check for
        # Returns: True if at least one word in the trie starts with the prefix, False otherwise
        # Time Complexity: O(m) where m is the length of the prefix
        # Space Complexity: O(1)
        curr = self.root

        # Traverse through each character in the prefix
        for ch in prefix:
            # If character doesn't exist in current node's children, no words with this prefix
            if ch not in curr.children:
                return False
            # Move to the child node for this character
            curr = curr.children[ch]

        # If we successfully traversed all prefix characters, the prefix exists
        return True


# Test the Trie implementation
if __name__ == "__main__":
    # Create a new Trie instance
    trie = Trie()

    # Define test operations to run
    operations = [
        ("insert", "apple"),    # Insert "apple" into trie
        ("search", "apple"),    # Search for complete word "apple" - should return True
        ("search", "app"),      # Search for "app" - should return False (prefix exists but not complete word)
        ("startsWith", "app"),  # Check if any word starts with "app" - should return True
        ("insert", "app"),      # Insert "app" as a complete word
        ("search", "app")       # Search for "app" again - should now return True
    ]

    # Execute operations and collect results
    results = []
    for op, word in operations:
        if op == "insert":
            trie.insert(word)
            result = None  # Insert operations don't return a value
        elif op == "search":
            result = trie.search(word)
        elif op == "startsWith":
            result = trie.startsWith(word)

        print(f"{op}('{word}') -> {result}")
        results.append(result)

    # Compare with expected output
    print("\nExpected output: [null, true, false, true, null, true]")
    print(f"Actual output: {[result for result in results]}")

    # Additional test cases to demonstrate functionality
    print("\nAdditional Tests:")
    trie.insert("hello")
    print(f"search('hell') -> {trie.search('hell')}")           # False - "hell" not inserted as complete word
    print(f"startsWith('hell') -> {trie.startsWith('hell')}")   # True - "hello" starts with "hell"
    print(f"search('hello') -> {trie.search('hello')}")         # True - "hello" was inserted as complete word