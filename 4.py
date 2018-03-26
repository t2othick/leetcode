# coding: utf8


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        text = '#'
        for x, y in zip(s, ['#'] * len(s)):
            text += x + y
        max_l = 1
        max_str = text[0]
        for i in range(len(text)):
            j = i - 1
            length = 1
            while j >= 0 and 2 * i - j < len(text):
                if text[j] == text[2 * i - j]:
                    length += 2
                    j -= 1
                else:
                    break
            if length > max_l:
                max_l = length
                max_str = text[(i - length/2): (i + length/2) + 1]
        return "".join([x for x in max_str if x != '#'])


if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome('abbc')
