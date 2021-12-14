# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        _sum = 0
        if root.val > low:
            _sum += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            _sum += self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            _sum += root.val
        return _sum