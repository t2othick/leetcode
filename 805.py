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
    def isFit(self, A, C, S):
        dp = []
        for i in range(len(A) + 1):
            x = []
            for j in range(C + 1):
                y = []
                for k in range(S + 1):
                    y.append(0)
                x.append(y)
            dp.append(x)

        for i in range(len(A) + 1):
            dp[i][0][0] = 1

        i = 1
        while i <= len(A):
            j = 1
            while j <= C and j <= i:
                k = 1
                while k <= S:
                    dp[i][j][k] = dp[i - 1][j][k]
                    if A[i - 1] <= k: dp[i][j][k] += dp[i - 1][j - 1][k - A[i - 1]]
                    k += 1
                j += 1
            i += 1

        return dp[len(A)][C][S] > 0

    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        c = len(A)
        ks = [0, ] * c

        for i in range(1, c):
            if s * i % c == 0:
                ks[i] = s * i / c

        for i in range(1, len(ks) - 1):
            if ks[i] == 0:
                continue
            if self.isFit(A, i, ks[i]):
                return True

        return False


print Solution().splitArraySameAverage([16, 19, 5, 0, 2, 3])
