class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        self.res = []
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])
        self.visited = [0 for x in range(numCourses)]
        for x in range(numCourses):
            if not self.dfs(x):
                return []
        return self.res
    
    def dfs(self, node):
        if self.visited[node]== -1:
            return False
        if self.visited[node]== 1:
            return True
        self.visited[node] = -1
        for x in self.graph[node]:
            if not self.dfs(x):
                return False
        self.visited[node] = 1
        self.res.append(node)
        return True