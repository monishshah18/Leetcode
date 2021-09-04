class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        count = [1]*n
        res = [0]*n
        trees = collections.defaultdict(set)
        for i,j in edges:
            trees[i].add(j)
            trees[j].add(i)
        def dfs(root, pre):
            for i in trees[root]:
                if i!=pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
        def dfs2(root, pre):
            for i in trees[root]:
                if i!=pre:
                    res[i] = res[root] - count[i] + n - count[i]
                    dfs2(i, root)
        dfs(0,-1)
        dfs2(0,-1)
        return res