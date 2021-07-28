class Solution:
    def minSwaps(self, s: str) -> int:
        n=len(s)
        zeroes = 0
        ones = 0
        for i in s:
            if i == '0':
                zeroes += 1
            else:
                ones += 1
        if abs(zeroes-ones) > 1:
            return -1
        if zeroes > ones:
            return self.minSwapsUtil(s, '0')
        elif ones > zeroes:
            return self.minSwapsUtil(s, '1')
        else:
            return min(self.minSwapsUtil(s, '0'),self.minSwapsUtil(s, '1'))
    def minSwapsUtil(self, s, c):
        count = 0
        for ch in s:
            if ch != c:
                count += 1
            c = '1' if c == '0' else '0'
        return count // 2
        