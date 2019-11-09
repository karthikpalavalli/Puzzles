# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        node = head

        while node.next.next is not None:
            if node.next.val == node.val:
                node.next = node.next.next

        return head
