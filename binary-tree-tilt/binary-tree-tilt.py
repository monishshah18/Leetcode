# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def tilt(root):
            if not root:
                return (0,0)
            _left = tilt(root.left)
            _right = tilt(root.right)
            return (_left[0]+_right[0]+root.val, abs(_left[0]-_right[0])+_left[1]+_right[1])
        return tilt(root)[1]