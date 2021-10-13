# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res = [float('inf')]
        def traverseTree(node):
            if not node:
                return
            if root.val < node.val < res[0]: #since root is always minimum so only right tree needs to be traversed.
                res[0] = node.val
            traverseTree(node.left)
            traverseTree(node.right)
        traverseTree(root)
        return -1 if res[0]==float('inf') else res[0]