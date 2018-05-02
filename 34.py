class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lower_index = self.lower_boundary(nums, target)
        upper_index = self.upper_boundary(nums, target)
        return [lower_index, upper_index]

    def lower_boundary(self, nums, target):
        if len(nums) == 0:
            return -1
        if nums[0] > target or nums[-1] < target:
            return -1
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
        return -1

    def upper_boundary(self, nums, target):
        if len(nums) == 0:
            return -1
        if nums[0] > target or nums[-1] < target:
            return -1
        start = 0
        end = len(nums) - 1
        while end - start > 1:
            mid = (start + end) / 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] <= target:
                start = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1


print Solution().searchRange([1,1], 1)