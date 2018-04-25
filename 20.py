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


class Stack(object):
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, o):
        self.stack.append(o)

    def pop(self):
        return self.stack.pop()

    def seak(self):
        return self.stack[-1]


class Solution(object):
    table = {')': '(', ']': '[', '}': '{'}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        for c in s:
            if stack.empty() or c not in self.table or stack.seak() != self.table[c]:
                stack.push(c)
            else:
                stack.pop()
        return stack.empty()


print Solution().isValid('([{}])[]{}')
