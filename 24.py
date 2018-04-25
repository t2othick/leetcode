class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        if not current:
            return current
        head = current.next
        if not head:
            return current
        keep_node3 = None
        while current is not None:
            current_1 = current
            current_2 = current_1.next if current_1 else None
            current_3 = current_2.next if current_2 else None
            current_4 = current_3.next if current_3 else None

            current = current_4.next if current_4 else None

            current_1.next = current_4 or current_3
            if current_2:
                current_2.next = current_1
            if current_4:
                current_4.next = current_3
            if keep_node3:
                keep_node3.next = current_2 or current_1
            keep_node3 = current_3
            if keep_node3:
                keep_node3.next = None

        return head
