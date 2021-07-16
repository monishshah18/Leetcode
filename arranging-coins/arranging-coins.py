class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1+(sqrt(1+(8*n))))/2)
        