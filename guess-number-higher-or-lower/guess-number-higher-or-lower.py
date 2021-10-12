# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower,upper = 1,n
        mid = (lower+upper)//2
        while guess(mid)!=0:
            if guess(mid)==1:
                lower = mid + 1
            else:
                upper = mid - 1
            mid = (lower+upper) >> 1
        return mid
            