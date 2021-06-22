class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return s1==s2 or sorted(s1)==sorted(s2) and sum(i!=j for i,j in zip(s1,s2))==2
        