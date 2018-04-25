class Solution(object):
    def plus(self, n):
        if n < 0:
            return n - n - n
        return n

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        flag = 1 if ((dividend >= 0 and divisor >= 0) or (dividend <= 0 and divisor <= 0)) else -1
        dividend = self.plus(dividend)
        divisor = self.plus(divisor)
        if dividend < divisor:
            return 0
        if dividend != 0 and dividend == divisor:
            return flag
        if divisor == 0:
            return -1
        sr = 0

        while (sr * divisor < dividend):
            r = 1
            tdivisor = divisor
            tdividend = dividend - sr * divisor
            while (tdivisor << 1) <= tdividend:
                tdivisor = tdivisor << 1
                r = r << 1
            sr += r

        sr =  sr - 1

        remainder = dividend - sr * divisor
        while(remainder - divisor >= 0):
            sr += 1
            remainder -= divisor
        sr = (sr if flag == 1 else (sr - sr - sr))
        return sr if sr <= 2147483647 else 2147483647
