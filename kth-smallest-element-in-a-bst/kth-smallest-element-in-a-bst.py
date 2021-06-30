# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []
        if not root: return
        def inorder(node):
            if not node:
                return
            if len(ans)==k:
                return
            inorder(node.left)
            if len(ans) < k:
                ans.append(node.val)
                inorder(node.right)
            else:
                return
        inorder(root)
        return ans[-1]
        