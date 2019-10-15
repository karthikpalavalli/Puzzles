class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        ptr1 = l1
        ptr2 = l2
        ptr_head = merged_list_head = ListNode(-1)

        while ptr1 is not None or ptr2 is not None:
            new_node = None

            if ptr2 is None or \
                    (ptr1 is not None and ptr1 is not None and ptr1.val <= ptr2.val):
                new_node = ListNode(ptr1.val)
                ptr1 = ptr1.next

            elif ptr1 is None or \
                    (ptr1 is not None and ptr2 is not None and ptr1.val > ptr2.val):
                new_node = ListNode(ptr2.val)
                ptr2 = ptr2.next

            ptr_head.next = new_node
            ptr_head = ptr_head.next

        return merged_list_head.next