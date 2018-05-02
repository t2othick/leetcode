# Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        new_head = local_head = None
        last_tail = current_node = head
        while current_node is not None:
            if count % k == 0:
                local_head = current_node
            if count % k == k - 1:
                local_new_head = current_node
                if count == k - 1:
                    new_head = current_node
                current_node = current_node.next
                local_current = local_head.next
                prev = local_head
                local_k = 0
                while local_k <= k - 2:
                    tmp = local_current.next
                    local_current.next = prev
                    prev = local_current
                    local_current = tmp
                    local_k += 1
                last_tail.next = local_new_head
                last_tail = local_head
            else:
                current_node = current_node.next
            count += 1
        if new_head is not None and (count - 1) % k < k - 1:
            last_tail.next = local_head
        elif new_head is not None and (count - 1) % k == k - 1:
            last_tail.next = None

        if new_head is None:
            return head
        return new_head


def make(nums):
    head = current = None
    for x in nums:
        if head is None:
            head = ListNode(x)
            current = head
        else:
            current.next = ListNode(x)
            current = current.next
    return head


def show(head):
    current = head
    while current is not None:
        print current.val
        current = current.next


if __name__ == '__main__':
    head = make(range(1, 5))
    show(head)

    print '-' * 10
    new_head = Solution().reverseKGroup(head, 2)
    show(new_head)