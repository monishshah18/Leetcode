class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for x in string.ascii_lowercase:
            i,j = s.find(x),s.rfind(x)
            if i > -1:
                res += len(set(s[i+1:j]))
        return res
        