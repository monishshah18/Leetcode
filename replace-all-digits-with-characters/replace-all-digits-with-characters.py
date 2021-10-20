class Solution:
    def replaceDigits(self, s: str) -> str:
        res = list(s)
        for i in range(1, len(res), 2):
            res[i] = chr(ord(res[i-1])+int(res[i]))
        return ''.join(res)