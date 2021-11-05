class Solution:
    def calculate(self, s: str) -> int:
        res,num,sign,stack = 0,0,1,[]
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i in ["+","-"]:
                res += num * sign
                num = 0
                sign = [-1,1][i=="+"]
            elif i == '(':
                stack.append(res)
                stack.append(sign)
                sign,res = 1,0
            elif i == ')':
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign