# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return (float("inf"), 0, 0)
            q1_l, q2_l, q3_l = dfs(node.left)
            q1_r, q2_r, q3_r = dfs(node.right)
            q1 = min(q1_l, q2_l) + min(q1_r, q2_r) + 1
            q3 = min(q1_l + q1_r, q1_l + q3_r, q3_l + q1_r)
            q2 = min(q3, q3_l + q3_r)
            return (q1, q2, q3)
            
        return min(dfs(root)[0::2]) 
        