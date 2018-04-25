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


class MyQueue(object):
    def __init__(self, size):
        self.size = size
        self.pool = []

    def push(self, o):
        self.pool.append(o)
        while len(self.pool) > self.size:
            self.pool = self.pool[1:]

    def head(self):
        if len(self.pool) > 0:
            v = self.pool[0]
            self.pool = self.pool[1:]
            return v
        return None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        my_queue = MyQueue(n + 1)
        current = head
        length = 0
        while current is not None:
            my_queue.push(current)
            current = current.next
            length += 1
        # print "test", length == n, head.next.val
        if length == n:
            return head.next
        h = my_queue.head()
        my_queue.head()
        t = my_queue.head()
        h.next = t
        return head


n1 = ListNode(5)
n2 = ListNode(4)
n2.next = n1
n3 = ListNode(3)
n3.next = n2
n4 = ListNode(2)
n4.next = n3
head = ListNode(1)
head.next = n4


def show(head):
    c = head
    while c is not None:
        print c.val
        c = c.next


# show(head)
head = Solution().removeNthFromEnd(head, 1)
# print "-" * 10
show(head)