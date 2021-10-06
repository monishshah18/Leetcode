# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev,curr,drops = TreeNode(float("-inf")), root, []
        while curr:
            if curr.left:
                temp = curr.left
                while temp.right and temp.right != curr:temp = temp.right
                if not temp.right:
                    temp.right,curr = curr,curr.left
                    continue
                temp.right = None
            if curr.val < prev.val: drops.append((prev,curr))
            prev,curr = curr, curr.right
        drops[0][0].val,drops[-1][-1].val = drops[-1][-1].val, drops[0][0].val
        