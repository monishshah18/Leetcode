class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = list(map(len, s.replace('01','0 1').replace('10','1 0').split()))
        return sum(min(i,j) for i,j in zip(s,s[1:]))