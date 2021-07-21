class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def cmp(a, b):
            return (a > b) - (a < b) 
        symbols = [(i,j) for i,j in enumerate(dominoes) if j != '.']
        symbols = [(-1,'L')]+symbols+[(len(dominoes),'R')]
        res = list(dominoes)
        for (i,x), (j,y) in zip(symbols,symbols[1:]):
            if x == y:
                for k in range(i+1,j):
                    res[k] = x
            elif x > y:
                for k in range(i+1,j):
                    res[k] = '.LR'[cmp(k-i, j-k)]
        return ''.join(res)