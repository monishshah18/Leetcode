class Solution:
    def makeFancyString(self, s: str) -> str:
        res,cnt = [],0
        for i,c in enumerate(s):
            if i > 0 and c == s[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                res.append(c)
        return ''.join(res)