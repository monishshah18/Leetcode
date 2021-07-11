# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        self.dfs(root, targetSum,[],res)
        return res
    def dfs(self, root, s, curr, res):
        curr.append(root.val)
        if root.val == s and not(root.left or root.right):
            res.append(curr)
        else:
            if root.left:
                self.dfs(root.left, s-root.val,curr[:],res)
            if root.right:
                self.dfs(root.right,s-root.val,curr[:],res)