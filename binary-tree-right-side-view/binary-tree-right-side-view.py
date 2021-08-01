# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_dict = {}
        level = 0
        self.rightSideRec(root, right_dict, level)
        return right_dict.values()
    def rightSideRec(self, root, right_dict, level):
        if not root:
            return
        right_dict[level] = root.val
        self.rightSideRec(root.left, right_dict, level+1)
        self.rightSideRec(root.right, right_dict, level+1)
        