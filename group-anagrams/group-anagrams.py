class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            res = str(''.join(sorted(s)))
            if not res in d:
                d[res] = [s]
            else:
                d[res].append(s)
        return list(d.values())