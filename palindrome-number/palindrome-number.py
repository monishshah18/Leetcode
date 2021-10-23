class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = str(x)[::-1]
        if ans == str(x):
            return True
        else:
            return False