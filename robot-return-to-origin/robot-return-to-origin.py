class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'U':0,'D':0,'L':0,'R':0}
        for i in moves:
            d[i] += 1
        return (d['U']==d['D'] and d['R']==d['L'])
        