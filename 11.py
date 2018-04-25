class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        area = 0
        while i != j:
            if height[i] < height[j]:
                area = area if (j - i) * height[i] < area else (j - i) * height[i]
                i += 1
            else:
                area = area if (j - i) * height[j] < area else (j - i) * height[j]
                j -= 1
        return area
