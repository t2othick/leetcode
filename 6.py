# coding: utf8


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        texts = ['', ] * numRows
        c_column = 0
        ps = 0
        while True:
            if ps >= len(s):
                break
            start = numRows - 2
            end = 0
            step = -1
            if c_column % 2 == 0:
                start = 0
                end = numRows
                step = 1
            while (step == 1 and start < end) or (step == -1 and start > end):
                texts[start] += (s[ps])
                start += step
                ps += 1
                if ps >= len(s):
                    break
            c_column += 1
        return "".join(texts)


if __name__ == "__main__":
    print Solution().convert('ABCDE', 4)
