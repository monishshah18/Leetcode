class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l+r)//2
            if sum((i+m-1)//m for i in piles) > h:
                l = m+1
            else:
                r = m
        return l