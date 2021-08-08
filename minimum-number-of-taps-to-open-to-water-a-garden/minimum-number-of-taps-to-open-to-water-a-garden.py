class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        for i,r in enumerate(ranges):
            l = max(0, i-r)
            ranges[l] = max(i+r, ranges[l])
        res = hi = lo = 0
        while hi < n:
            lo, hi = hi, max(ranges[lo:hi+1])
            if hi == lo: return -1
            res += 1
        return res