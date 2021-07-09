class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while (n > 1):
            if n%3 == 0:
                n /= 3
            else:
                break
        if n==1:
            return True
        return False
        