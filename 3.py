class Solution(object):

    @staticmethod
    def bigger(a, b):
        return a if a > b else b


    def lengthOfLongestSubstring(self, s):

        pos = {}
        max_length = start = 0
        input_length = len(s)
        for i in range(0, input_length):

            if s[i] in pos:
                max_length = Solution.bigger(max_length, i - start)
                start = Solution.bigger(pos[s[i]] + 1, start)

            pos[s[i]] = i

        return Solution.bigger(max_length, input_length - start)
