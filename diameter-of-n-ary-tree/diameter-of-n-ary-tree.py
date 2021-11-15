"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    def dfs(self, root):
        first = second = 0
        for neighbour in root.children:
            depth = self.dfs(neighbour)
            if depth > first:
                first, second = depth, first
            elif depth > second:
                second = depth
        self.diameter = max(self.diameter, first+second)
        return first + 1