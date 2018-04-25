class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        nums = height
        left_i = 0
        right_i = len(nums) - 1

        left_max = 0
        right_max = 0

        s = 0
        while left_i < right_i:
            if nums[left_i] > left_max:
                left_max = nums[left_i]
            if nums[right_i] > right_max:
                right_max = nums[right_i]

            if left_max < right_max:
                left_i += 1
                s += (0 if nums[left_i] > left_max else (left_max - nums[left_i]))
            else:
                right_i -= 1
                s += (0 if nums[right_i] > right_max else (right_max - nums[right_i]))

        return s
