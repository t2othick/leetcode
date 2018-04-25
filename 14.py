class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_length = len(strs[0])
        for content in strs:
            if len(content) < min_length:
                min_length = len(content)

        i = 0
        prefix = ""
        while i < min_length:
            flag = strs[0][i]
            for content in strs:
                if content[i] != flag:
                    return prefix
            prefix += flag
            i += 1
        return prefix
