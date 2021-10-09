class Solution:
    def removeDuplicates(self, s: str) -> str:
        for i in s:
            s = s.replace(i*2,"") if i in s else s
        return s