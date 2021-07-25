class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        
        return len(set(d.values()))== 1