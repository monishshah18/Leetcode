ch2oper = {'+':operator.add,'-':operator.sub,'*':operator.mul}
class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ways = []
        for i,j in enumerate(expression):
            if j in ch2oper:
                for left in self.diffWaysToCompute(expression[:i]):
                    for right in self.diffWaysToCompute(expression[i+1:]):
                        way = ch2oper[j](left,right)
                        ways.append(way)
        if not ways:
            return [int(expression)]
        return ways
        