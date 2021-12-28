class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for i in sentences:
            res = max(res, i.count(" ")+ 1)
        return res