class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.map:
                newNode = TrieNode()
                curr.map[char] = newNode
            curr = curr.map[char]
        curr.endOfWord = True

        

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.map:
                return False
            curr = curr.map[char]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.map:
                return False
            curr = curr.map[char]
        return True
        
class TrieNode:
    def __init__(self):
        self.map = {}
        self.endOfWord = False
