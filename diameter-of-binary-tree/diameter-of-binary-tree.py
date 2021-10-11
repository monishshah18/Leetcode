# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def longest_path(node):
            if not node:
                return 0
            left,right = longest_path(node.left),longest_path(node.right)
            self.diameter = max(self.diameter, left+right)
            return 1 + max(left, right)
        longest_path(root)
        return self.diameter