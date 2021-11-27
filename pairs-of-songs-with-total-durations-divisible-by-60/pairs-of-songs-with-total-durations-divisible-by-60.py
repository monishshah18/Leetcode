class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0]*60
        res = 0
        for t in time:
            res += count[-t % 60]
            count[t % 60] += 1
        return res