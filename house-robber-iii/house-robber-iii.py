# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0,0
            left, right = dfs(node.left), dfs(node.right)
            take = node.val + left[1] + right[1]
            not_take = max(left) + max(right)
            return take,not_take
        return max(dfs(root))