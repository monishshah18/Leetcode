class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for i in word:
            current = current.children[i]
        current.is_word = True
        

    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            current = current.children.get(i)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            current = current.children.get(i)
            if current is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)