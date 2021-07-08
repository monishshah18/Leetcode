class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = pattern[i]
            elif d[s[i]] != pattern[i]:
                return False
        return len(set(pattern)) == len(set(d.keys()))