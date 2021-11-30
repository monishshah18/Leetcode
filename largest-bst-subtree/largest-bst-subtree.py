# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.res = 0
        self.helper(root)
        return self.res
    def helper(self, root):
        if root:
            lres, lcount, lLow, lUpp = self.helper(root.left)
            rres, rcount, rLow, rUpp = self.helper(root.right)

            if lres and rres and lUpp < root.val < rLow:
                self.res = max(self.res, lcount + rcount + 1)
                return True, lcount + rcount + 1, min(lLow, root.val), max(root.val, rUpp)
            else:
                return False, 0, min(lLow, root.val, rLow), max(lUpp, root.val, rUpp)            
        else:
            return True, 0, float('inf'), float('-inf')