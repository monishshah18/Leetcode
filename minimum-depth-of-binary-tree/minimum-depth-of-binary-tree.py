# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if None in [root.left,root.right]:
            return max(self.minDepth(root.left),self.minDepth(root.right))+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1