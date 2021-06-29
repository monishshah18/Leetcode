class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        a = Counter(s)
        for i in a:
            if a[i] == 1:
                return s.index(i)
            else:
                pass
        return -1
        
        