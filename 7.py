class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > 0 else -1
        x = x if x > 0 else -x

        s = 0
        while x > 0:
            s = s * 10 + x % 10
            x /= 10

        if (flag == 1 and s > 2147483647L) or (flag == -1 and s > 2147483648L):
            return 0
        return s * flag
