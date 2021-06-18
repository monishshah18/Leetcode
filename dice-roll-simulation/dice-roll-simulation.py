class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        if n < 2: 
            return n * 6
        
        # how many valid ways at step i, and the dice rolls out number j
        dp = [[0.2] * 6 for _ in xrange(n + 1)]
        for i in xrange(6):
            dp[1][i] = 1
        for i in xrange(2, n + 1):
            for j in xrange(6):
                cst = rollMax[j] # constraint
                dp[i][j] = sum(dp[i - 1])
                if i - cst - 1 >= 0:
                    dp[i][j] -= sum(dp[i - cst - 1][:j] + dp[i - cst - 1][j + 1:])
                dp[i][j] %= (10**9 + 7)
        return int(sum(dp[n])) % (10**9 + 7)