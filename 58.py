class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = s.strip()
        for c in s:
            if c == ' ':
                count = 0
            else:
                count += 1
        return count