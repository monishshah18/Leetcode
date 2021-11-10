class Solution:
    diameter = 0
    def treeDiameter(self, edges: List[List[int]]) -> int:
        def dfs(node, pre):
            d1 = d2 = 0
            for nex in graph[node]:
                if nex != pre:
                    d = dfs(nex, node)
                    if d > d1:
                        d1, d2 = d, d1
                    elif d > d2:
                        d2 = d
            self.diameter = max(self.diameter, d1+d2)
            return d1 + 1
        graph = defaultdict(set)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        dfs(0, None)
        return self.diameter