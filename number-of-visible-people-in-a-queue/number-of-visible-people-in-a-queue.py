class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n,stack = len(heights),[]
        ans = [0]*n
        for i,j in enumerate(reversed(heights)):
            while stack and j > stack[-1]:
                stack.pop()
                ans[i] += 1
            if stack:
                ans[i] += 1
            stack.append(j)
        return ans[::-1]