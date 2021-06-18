class Solution:
    def reverseWords(self, s: str) -> str:
        return (' '.join([s[::-1] for s in s.split(" ")]))
        