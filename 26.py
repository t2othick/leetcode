class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        j = 1
        current = nums[0]
        length = 1
        for i in range(1, len(nums)):
            if nums[i] == current:
                continue
            else:
                current = nums[i]
                nums[j] = current
                j += 1
                length += 1
        return length
