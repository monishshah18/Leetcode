class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitDict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 0:
            oldList = []
        else:
            oldList = ['']
            for i in digits:
                newList = []
                for j in digitDict[i]:
                    newList.extend([k+j for k in oldList])
                oldList = newList
        return oldList