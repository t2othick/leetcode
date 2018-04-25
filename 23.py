class Solution(object):
    def adjust_heap(self, nodes, index):
        while index < len(nodes):
            li = 2 * index + 1
            ri = 2 * index + 2
            min_index = index
            if li < len(nodes) and nodes[li].val < nodes[index].val:
                min_index = li
            if ri < len(nodes) and nodes[ri].val < nodes[min_index].val:
                min_index = ri
            if min_index != index:
                tmp = nodes[min_index]
                nodes[min_index] = nodes[index]
                nodes[index] = tmp
                index = min_index
            else:
                return nodes
        return nodes

    def make_heap(self, nodes):
        length = len(nodes)
        for i in range(length / 2 + 1, -1, -1):
            nodes = self.adjust_heap(nodes, i)
        return nodes

    def find_min(self, nodes):
        minest = nodes[0]
        if minest.val == 2 ** 32:
            return None
        return minest


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        new_lists = []
        for l in lists:
            if l:
                new_lists.append(l)
        lists = new_lists
        if len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]

        current_nodes = []
        for l in lists:
            current_nodes.append(l)
        current_nodes = self.make_heap(current_nodes)

        head = ListNode(-1)
        current = head
        while True:
            node = self.find_min(current_nodes)
            if node is None:
                break
            current.next = ListNode(node.val)
            if node.next is not None:
                current_nodes[0] = node.next
            else:
                current_nodes[0] = ListNode(2 ** 32)
            self.adjust_heap(current_nodes, 0)
            current = current.next
        return head.next
