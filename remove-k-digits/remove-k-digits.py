class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and k > 0 and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)
        while stack and k > 0:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        return str(int(''.join(stack)))
        