class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        A,B = a,b
        while B:
            A,B = B, A % B
        l,r,lcm = 2, 10**14, a*b//A
        while l < r:
            m = (l + r)//2
            if m // a + m // b - m // lcm < n:
                l = m + 1
            else:
                r = m
        return l % (10**9 + 7)