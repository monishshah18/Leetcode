class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')' and stack:
                stack.pop()
            elif s[i]==')':
                s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)