class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        tree = defaultdict(list)
        for i,j in enumerate(prevRoom): tree[j].append(i)
        print(tree)
        def fn(n):
            if not tree[n]: 
                return 1,1
            c, m = 0, 1
            for nn in tree[n]:
                cc, mm = fn(nn)
                c += cc
                m = (m * comb(c, cc) * mm) % 1_000_000_007
            return c+1, m
        return fn(0)[1]
        