class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0
        for i in s:
            if right==0 and i == ')':
                left += 1
            else:
                right += 1 if i == '(' else -1
        return left+right