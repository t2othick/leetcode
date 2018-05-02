#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Zhihu
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

""" Say Something Here"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums = sorted(nums)
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums, i + 1, len(nums) - 1, nums[i])
        return self.res

    def twoSum(self, nums, start, end, target):
        while start < end:
            if nums[start] + nums[end] + target < 0:
                start += 1
            elif nums[start] + nums[end] + target > 0:
                end -= 1
            else:
                self.res.append([target, nums[start], nums[end]])
                while start < end and nums[start] == nums[start+1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1
                start += 1
                end -= 1


print Solution().threeSum([-1, 0, 1, 2, -1, -4])
