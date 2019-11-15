from collections import defaultdict

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptr_A = headA
        map_A = defaultdict(int)

        while ptr_A:
            map_A[ptr_A] = 1

            ptr_A = ptr_A.next

        ptr_B = headB

        while ptr_B:
            if map_A[ptr_B]:
                return ptr_B

            ptr_B = ptr_B.next
