class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        start = 0
        end = len(nums) - 1
        while end - start > 1:
            mid = (start + end) / 2
            if nums[mid] >= target:
                end = mid
            elif nums[mid] < target:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return end


print Solution().searchInsert([1, 3], 3)