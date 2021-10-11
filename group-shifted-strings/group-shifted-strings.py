class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = {}
        for s in strings:
            key = ()
            for i in range(len(s)-1):
                circular_diff = 26 + ord(s[i+1])-ord(s[i])
                key += circular_diff % 26,
            d[key] = d.get(key, []) + [s]
        return list(d.values())