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
    def f(self, digits, nums, step, text=""):
        if len(digits) == 0:
            return
        if len(text) == len(digits):
            self.res.append(text)
            return
        for x in nums[digits[step]]:
            self.f(digits, nums, step + 1, text + x)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.res = []
        nums = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.f(digits, nums, 0)
        return self.res

print Solution().letterCombinations('23')
print Solution().letterCombinations('24')
print Solution().letterCombinations('23546789')
