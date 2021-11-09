class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        SIZE = 26
        trie = [[0]*SIZE]
        count = [0]
        for word in words:
            word = sorted(set(word))
            if len(word) <= 7:
                node = 0
                for letter in word:
                    i = ord(letter) - ord('a')
                    if trie[node][i] == 0:
                        trie.append([0]*SIZE)
                        count.append(0)
                        trie[node][i] = len(trie) - 1
                    node = trie[node][i]
                count[node] += 1
        def dfs(node, has_first):
            total = count[node] if has_first else 0
            for letter in puzzle:
                i = ord(letter) - ord('a')
                if trie[node][i]:
                    total += dfs(trie[node][i], has_first or letter == puzzle[0])
            return total
        result = []
        for puzzle in puzzles:
            result.append(dfs(0, False))
        return result