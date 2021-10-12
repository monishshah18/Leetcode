class Solution:
    def minDifference(self, nums: List[int]) -> int:
        return min(i-j for i,j in zip(heapq.nlargest(4,nums), heapq.nsmallest(4, nums)[::-1]))