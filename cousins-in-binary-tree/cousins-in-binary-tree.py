# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node,parent,level,mod):
            if node:
                if node.val==mod:
                    return level,parent
                return dfs(node.left,node,level+1,mod) or dfs(node.right,node,level+1,mod)
        dx,px,dy,py = dfs(root,None,0,x) + dfs(root,None,0,y)
        return dx==dy and px!=py