class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        def dfs(merge, w1, w2):
            if not w1 or not w2:
                return merge + (w1 if w1 else w2)
            if w1 >= w2:
                return dfs(merge + w1[0], w1[1:], w2)
            elif w1 < w2:
                return dfs(merge + w2[0], w1, w2[1:])
        return dfs("", word1, word2)