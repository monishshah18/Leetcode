# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        from hashlib import sha256
        def hash_(x):
            S = sha256()
            S.update(x.encode('utf-8'))
            return S.hexdigest()
        
        def merkle(node):
            if not node:
                return '#'
            n_left = merkle(node.left)
            n_right = merkle(node.right)
            node.merkle = hash_(n_left+str(node.val)+n_right)
            count[node.merkle].append(node)
            return node.merkle
        count = collections.defaultdict(list)
        merkle(root)
        return [node.pop() for node in count.values() if len(node) >= 2]