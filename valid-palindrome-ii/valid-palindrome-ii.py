class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i < j:
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                return self.util(s,i,j-1) or self.util(s,i+1,j)
        return True
    
    def util(self, s, i, j):
        while i < j:
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True