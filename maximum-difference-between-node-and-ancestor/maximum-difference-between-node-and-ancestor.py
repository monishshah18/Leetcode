# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxDiff = 0
        def dfs(node, low, high):
            if not node: return
            self.maxDiff = max(self.maxDiff, abs(node.val - low), abs(node.val - high))
            low1, high1 = min(low, node.val), max(high, node.val)
            dfs(node.left, low1, high1)
            dfs(node.right, low1, high1)
        dfs(root, root.val, root.val)
        return self.maxDiff