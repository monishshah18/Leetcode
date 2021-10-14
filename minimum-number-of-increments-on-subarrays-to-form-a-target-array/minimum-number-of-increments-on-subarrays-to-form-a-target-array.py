class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res,pre = 0,0
        for t in target:
            res += max(t-pre,0)
            pre = t
        return res