class Solution:
    def minTimeToType(self, word: str) -> int:
        res = len(word)
        prev = "a"
        for i in word:
            val = (ord(i) - ord(prev)) % 26
            res += min(val, 26-val)
            prev = i
        return res