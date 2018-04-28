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
    def is_closest(self, target, current, next):
        if abs(target - current) < abs(target - next):
            return False
        return True

    def twoSum(self, nums, first, start, end, target):
        closest = nums[first] + nums[start] + nums[end]
        while start < end:
            i_closest = nums[first] + nums[start] + nums[end]
            # print 'test', target, i_closest, nums[first] + nums[start] + nums[end-1]
            while start < end - 1 and self.is_closest(target, i_closest, nums[first] + nums[start] + nums[end-1]):
                i_closest = nums[first] + nums[start] + nums[end-1]
                end -= 1
            if self.is_closest(target, closest, i_closest):
                closest = i_closest
            start += 1
        return closest


    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        # print nums
        closest = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            i_closest = self.twoSum(nums, i, i + 1, len(nums) - 1, target)
            if self.is_closest(target, closest, i_closest):
                closest = i_closest
        return closest


print Solution().threeSumClosest([6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10], -52)
