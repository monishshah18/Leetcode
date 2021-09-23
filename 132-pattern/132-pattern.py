class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, maxMid = [],float('-inf')
        for n in nums[::-1]:
            if n < maxMid: return True
            while stack and stack[-1] < n:
                maxMid = stack.pop()
            stack += n,
        return False