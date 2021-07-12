class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                sq = i*i + j*j
                res = int(sq**0.5)
                if (res*res == sq and res<=n):
                    c += 2
        return c
        