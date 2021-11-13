class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                curr = stack.pop()
                res[curr] = i - curr
            stack.append(i)
        return res