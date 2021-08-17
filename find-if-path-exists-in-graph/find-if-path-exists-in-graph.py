class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited = [False]*n
        d = {}
        for i in edges:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]
            if i[1] in d:
                d[i[1]].append(i[0])
            else:
                d[i[1]] = [i[0]]
        q = [start]
        while q:
            curr = q.pop(0)
            if curr == end:
                return True
            elif curr in d and not visited[curr]:
                q.extend(d[curr])
            visited[curr] = True
        return False