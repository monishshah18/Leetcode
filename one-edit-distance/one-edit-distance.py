class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s==t:
            return False
        i = 0
        while i < min(len(s),len(t)):
            if s[i]==t[i]:
                i += 1
            else:
                break
        return s[i+1:]==t[i+1:] or s[i:]==t[i+1:] or s[i+1:]==t[i:]