# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def order(root, dic):
            if not root:
                return 0
            left = order(root.left,dic)
            right = order(root.right,dic)
            level = max(left,right)+1
            dic[level] += root.val,
            return level
        dic = defaultdict(list)
        res = []
        order(root, dic)
        for i in range(1, len(dic)+1):
            res.append(dic[i])
        return res