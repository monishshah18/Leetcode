class Solution:
    def canWinNim(self, n: int) -> bool:
        if n > 99:
            n = int(str(n)[-2:])
        return bool(n%4)
        