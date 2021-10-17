# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.numberPaths = 0
        self.dfs(root, targetSum)
        return self.numberPaths
    
    def dfs(self, node, target):
        if node is None:
            return
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
    
    def test(self, node, t):
        if node is None:
            return
        if node.val == t:
            self.numberPaths += 1
        self.test(node.left, t-node.val)
        self.test(node.right, t-node.val)