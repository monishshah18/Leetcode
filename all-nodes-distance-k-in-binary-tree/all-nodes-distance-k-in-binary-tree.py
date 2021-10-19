# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node,0)
                return 1
            else:
                L,R = dfs(node.left),dfs(node.right)
                if L != -1:
                    if L==k:
                        ans.append(node.val)
                    subtree_add(node.right, L+1)
                    return L+1
                elif R != -1:
                    if R==k:
                        ans.append(node.val)
                    subtree_add(node.left, R+1)
                    return R+1
                else:
                    return -1
        def subtree_add(node, distance):
            if not node:
                return
            elif distance==k:
                ans.append(node.val)
            else:
                subtree_add(node.left, distance+1)
                subtree_add(node.right, distance+1)
        dfs(root)
        return ans