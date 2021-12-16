class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        G = defaultdict(set)
        seen = [False]*n
        for u,v in edges:
            G[u].add(v)
            G[v].add(u)
        def dfs(i):
            if seen[i]:
                return []
            seen[i] = True
            longestPath = max((dfs(adj) for adj in G[i]),key=len,default=[]) + [i]
            seen[i] = False
            return longestPath
        path = dfs(dfs(0)[0])
        return set([path[len(path)//2],path[(len(path)-1)//2]])