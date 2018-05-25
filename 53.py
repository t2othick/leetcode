class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = max_value = nums[0]
        for i in range(1, len(nums)):
            current = max(prev + nums[i], nums[i])
            if current > max_value:
                max_value = current
            prev = current
        return max_value


print Solution().maxSubArray([-2, 1, 2])