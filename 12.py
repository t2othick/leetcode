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


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 400: 'CD', 900: 'CM', 40: 'XL',
                     50: 'L', 90: 'XC', 100: 'C', 1000: 'M', 500: 'D'}
        nums = sorted(nums_dict.keys(), reverse=True)
        i = 0
        s = ""
        while num > 0:
            # print i, nums, num
            if nums[i] <= num:
                s += nums_dict[nums[i]]
                num -= nums[i]
            else:
                i += 1

        return s


if __name__ == '__main__':
    print Solution().intToRoman(1994)
