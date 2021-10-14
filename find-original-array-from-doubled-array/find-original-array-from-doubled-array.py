class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ch = collections.Counter(changed)
        if ch[0]%2:
            return []
        for x in sorted(ch):
            if ch[x] > ch[2*x]:
                return []
            ch[2*x] -= ch[x] if x else ch[x]//2
        return list(ch.elements())