# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_, pre_ = root.val, None
        stack, sums = collections.deque(), collections.deque()
        while stack or root:
            while root:
                stack.append(root)
                sums.append(root.val)
                root = root.left
            root = stack[-1].right
            if not root or root is pre_:
                root, pre_, sum_ = None, stack.pop(), sums.pop()
                if sum_ > max_:
                    max_ = sum_
                if stack and sum_ > 0:
                    if stack[-1].left is pre_:
                        sums[-1] += sum_
                    else:
                        if sum_ + sums[-1] > max_:
                            max_ = sum_ + sums[-1]
                        if sum_ + stack[-1].val > sums[-1]:
                            sums[-1] = sum_ + stack[-1].val
        return max_