class Solution:
    def numSplits(self, s: str) -> int:
        left_ways = collections.Counter()
        right_ways = collections.Counter(s)
        
        res = 0
        for c in s:
            left_ways[c] += 1
            right_ways[c] -= 1
            
            if right_ways[c] == 0:
                del right_ways[c]
            if len(left_ways) == len(right_ways):
                res += 1
        return res
        