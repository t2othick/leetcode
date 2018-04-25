class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1
        while index > 0 and nums[index] <= nums[index - 1]:
            index -= 1
        index = index - 1
        if index != -1:

            min_index = index + 1
            for i in range(index + 1, len(nums)):
                if nums[index] < nums[i] <= nums[min_index]:
                    min_index = i

            tmp = nums[index]
            nums[index] = nums[min_index]
            nums[min_index] = tmp
        start = index + 1
        end = len(nums) - 1
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1
