class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = -1 if((dividend < 0) ^ (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        temp = 0
        for i in range(31, -1, -1):
            if (temp + (divisor << i) <= dividend):
                temp += (divisor << i)
                quotient |= 1 << i
        return sign  * quotient
        