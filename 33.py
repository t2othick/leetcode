class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        least_index = self.search_least(nums)
        if least_index == 0:
            return self.search_target(nums, target)
        if target >= nums[0]:
            return self.search_target(nums[:least_index], target)
        offset = self.search_target(nums[least_index:], target)
        if offset == -1:
            return -1
        return least_index + offset

    def search_least(self, nums):
        start = 0
        end = len(nums) - 1
        while end - start > 1:
            mid = (start + end) / 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
            # print start, end
        return start if nums[start] < nums[end] else end

    def search_target(self, nums, target):
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
            elif nums[mid] < target:
                start = mid
            else:
                return mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1


print Solution().search([1], 1)