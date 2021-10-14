class Solution:
    def numSquares(self, n: int) -> int:
        options = []
        for i in range(1, n+1):
            sqr = sqrt(i)
            if int(sqr)==sqr:
                options.append(i)
        min_ways = [float('inf')]*(n+1)
        min_ways[0] = 0
        for i in range(n+1):
            for opt in options:
                if opt <= i:
                    min_ways[i] = min(min_ways[i], 1 + min_ways[i-opt])
        return min_ways[-1]