class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = num
        for i in reversed(num):
            if (int(i))%2 == 0:
                res = res[:-1]
            else:
                break
        return res
            
        