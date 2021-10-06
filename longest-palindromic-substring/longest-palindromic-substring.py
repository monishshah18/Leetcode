class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            #for odd strings
            temp = self.helper(s,i,i)
            
            if len(temp) > len(res):
                res = temp
            #for even strings    
            temp = self.helper(s,i,i+1)
            
            if len(temp) > len(res):
                res = temp
        return res
    
    def helper(self,s,l,r):
        while l >= 0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]