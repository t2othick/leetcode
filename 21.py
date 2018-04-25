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


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        head = ListNode(-1)
        ph = head
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                head.next = p1
                p1 = p1.next
            else:
                head.next = p2
                p2 = p2.next
            head = head.next
        while p1 is not None:
            head.next = p1
            p1 = p1.next
            head = head.next
        while p2 is not None:
            head.next = p2
            p2 = p2.next
            head = head.next

        return ph.next


n4 = ListNode(3)
head1 = ListNode(-9)
head1.next = n4


nn4 = ListNode(7)
head2 = ListNode(5)
head2.next = nn4

x = Solution().mergeTwoLists(head1, head2)


def show(head):
    c = head
    while c is not None:
        print c.val
        c = c.next

show(x)