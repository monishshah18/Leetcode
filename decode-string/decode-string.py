class Solution:
    def decodeString(self, s: str) -> str:
        i,res,stack = 0,"",[]
        for j in s:
            if j == '[':
                stack.extend([i,res])
                i,res = 0,''
            elif j == ']':
                res = stack.pop() + stack.pop()*res
            elif j.isdigit():
                i = i*10 + int(j)
            else:
                res += j
        return res