# coding: utf8


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        text = str.strip()
        if len(text) == 0:
            return 0
        flag = 1
        if text[0] == '-':
            flag = -1
            text = text[1:]
        elif text[0] == '+':
            flag = 1
            text = text[1:]
        numString = ""
        for c in text:
            if '0' <= c <= '9':
                numString += c
            else:
                break
        # text = "".join([c for c in text if ('0' <= c <= '9')])
        if len(numString) == 0:
            return 0
        num = flag * int(numString)
        if num >= 2147483647:
            return 2147483647
        if num <= -2147483648:
            return -2147483648
        return num


if __name__ == "__main__":
    print Solution().myAtoi("  - 321")
