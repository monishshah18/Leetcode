class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res, ct = 0, Counter
        chars_count = ct(chars)
        for i in words:
            word_count = ct(i)
            if all(word_count[c] <= chars_count[c] for c in word_count):
                res += len(i)
        return res
            