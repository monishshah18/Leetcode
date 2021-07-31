class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAlt = 0
        maxAlt = 0
        for i in range(0, len(gain)):
            currAlt += gain[i]
            maxAlt = max(maxAlt, currAlt)
        return maxAlt