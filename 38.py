class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = 1
        if n == 1:
            return str(num)
        for i in range(2, n + 1):
            num = self.has_next(num)
        return str(num)

    def has_next(self, n):
        res = ""
        count = 1
        prev = -1
        while n > 0:
            tail = n % 10
            n = n / 10
            if tail == prev:
                count += 1
            else:
                if prev != -1:
                    res = str(count) + str(prev) + res
                prev = tail
                count = 1
        if count != 0:
            res = str(count) + str(prev) + res
        return int(res)



print Solution().countAndSay(5)