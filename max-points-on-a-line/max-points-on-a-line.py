def find_slope(p1, p2):
    return atan2(p1[0]-p2[0],p1[1]-p2[1])
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1: return n
        m = 0
        for i in range(n):
            slope = []
            same = 0
            for j in range(n):
                if (j==i): continue
                if (points[i] == points[j]): same+=1
                slope.append(find_slope(points[i],points[j]))
            m = max(m, max(Counter(slope).values())+same+1)
        return m
        