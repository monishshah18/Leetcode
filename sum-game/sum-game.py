class Solution:
    def sumGame(self, num: str) -> bool:
        return sum([1,-1][i < len(num) / 2]*(4.5 if j=='?' else int(j)) for i,j in enumerate(num))!=0
        