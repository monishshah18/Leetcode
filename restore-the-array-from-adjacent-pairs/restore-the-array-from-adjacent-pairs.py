class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj,ans,n = defaultdict(list),[],len(adjacentPairs) + 1
        for a,b in adjacentPairs:
            adj[a] += [b]
            adj[b] += [a]
        for i,j in adj.items():
            if len(j) == 1:
                ans.append(i)
                break
        prev = -math.inf
        while len(ans) < n:
            for _next in adj.pop(ans[-1]):
                if _next != prev:
                    prev = ans[-1]
                    ans.append(_next)
                    break
        return ans
                    