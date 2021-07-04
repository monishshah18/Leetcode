class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==1: return [0,1]
        pre = self.grayCode(n-1)
        res = pre + [i+2**(n-1) for i in pre[::-1]]
        return res
        