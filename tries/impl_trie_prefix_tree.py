# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:
    def __init__(self):
        # Initialize the trie with an empty dictionary
        # Each key is a character, and each value is another dictionary
        self.root = {}

    def insert(self, word: str) -> None:
        # Start from the root node
        node = self.root

        # Traverse the trie character by character
        for char in word:
            # If the character doesn't exist in the current node,
            # create a new node (dictionary) for it
            if char not in node:
                node[char] = {}

            # Move to the next node
            node = node[char]

        # Mark the end of a word with a special character
        node['$'] = True

    def search(self, word: str) -> bool:
        # Start from the root node
        node = self.root

        # Traverse the trie character by character
        for char in word:
            # If character doesn't exist, the word is not in the trie
            if char not in node:
                return False

            # Move to the next node
            node = node[char]

        # Check if this is the end of a word
        # (if the special end marker exists)
        return '$' in node

    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        node = self.root

        # Traverse the trie character by character
        for char in prefix:
            # If character doesn't exist, no word starts with the prefix
            if char not in node:
                return False

            # Move to the next node
            node = node[char]

        # If we made it through all characters in the prefix,
        # then there exists at least one word with this prefix
        return True

    # Create a new Trie
trie = Trie()

# Run operations
operations = [
    ("insert", "apple"),
    ("search", "apple"),
    ("search", "app"),
    ("startsWith", "app"),
    ("insert", "app"),
    ("search", "app")
]

results = []
for op, word in operations:
    if op == "insert":
        trie.insert(word)
        result = None
    elif op == "search":
        result = trie.search(word)
    elif op == "startsWith":
        result = trie.startsWith(word)

    print(f"{op}('{word}') -> {result}")
    results.append(result)

print("\nExpected output: [null, true, false, true, null, true]")
print(f"Actual output: {[result for result in results]}")

# You can also add your own test cases here
print("\nAdditional Tests:")
trie.insert("hello")
print(f"search('hell') -> {trie.search('hell')}")
print(f"startsWith('hell') -> {trie.startsWith('hell')}")
print(f"search('hello') -> {trie.search('hello')}")