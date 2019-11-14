# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node_ptr = head

        while node_ptr.next is not None:
            if node_ptr.next.val == val:
                node_ptr.next = node_ptr.next.next

            node_ptr = node_ptr.next

        return head
