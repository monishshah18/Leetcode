class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][edges[0][1] in edges[1]]