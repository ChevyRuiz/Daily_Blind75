class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.map:
                newNode = TrieNode()
                curr.map[char] = newNode
            curr = curr.map[char]
        curr.endOfWord = True   

    def search(self, word: str) -> bool:
        curr = [self.root]
        for char in word:
            if char == '.':
                curr = [child for node in curr for child in node.map.values()]
                continue
            else:
                temp = []
                for node in curr:
                    if char in node.map:
                        temp.append(node.map[char])
                curr = temp
        return any(node.endOfWord for node in curr)

        
class TrieNode:
    def __init__(self):
        self.map = {}
        self.endOfWord = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
