# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorder(root):
            if root is None: return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
            
        def balanceT(l,r):
            if l > r: return None
            mid = (l+r)//2
            root = nodes[mid]
            root.left = balanceT(l,mid-1)
            root.right = balanceT(mid+1,r)
            return root
        inorder(root)
        return balanceT(0, len(nodes)-1)