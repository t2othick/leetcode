class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return False

        tmp = x
        s = 0
        while x > 0:
            s = s * 10 + x % 10
            x /= 10

        if s > 2147483647L:
            return tmp == 0
        return tmp == s
