class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def lessEq(x):
            return sum([min(x//i, n) for i in range(1, m+1)]) >= k
        beg, end = 1, m*n
        while beg < end:
            mid = (beg+end)//2
            if not lessEq(mid):
                beg = mid + 1
            else:
                end = mid
        return beg
        
        