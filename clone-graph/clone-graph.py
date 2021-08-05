"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        di = {}
        di[node.val] = Node(node.val)
        queue = []
        queue.append(node)
        while queue:
            curr = queue.pop(0)
            for neig in curr.neighbors:
                if neig.val not in di:
                    di[neig.val] = Node(neig.val)
                    queue.append(neig)
                di[curr.val].neighbors.append(di[neig.val])
        return di[node.val]
            