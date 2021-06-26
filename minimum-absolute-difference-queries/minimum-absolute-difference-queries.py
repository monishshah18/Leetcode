class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        counters = [Counter()]
        
        for i in nums:
            counters.append(Counter(counters[-1]))
            counters[-1][i] += 1
        ans = []
        for u,v in queries:
            a,b = float('inf'), float('-inf')
            for k in sorted(counters[v+1]-counters[u]):
                a, b = min(a, k-b),k
            ans.append(a if a < float('inf') else -1)
        return ans
        