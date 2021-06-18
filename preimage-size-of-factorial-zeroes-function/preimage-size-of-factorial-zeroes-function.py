class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(x):
            count = 0
            while x:
                x = x//5
                count += x
            return count
        start, end = 0, 2**63 - 1
        while start < end:
            mid = (start+end)//2
            if f(mid) < k:
                start = mid + 1
            else:
                end = mid
        return 5 if f(start) == k else 0
            
        