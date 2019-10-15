class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow_runner = head
        fast_runner = head

        while fast_runner is not None or fast_runner.next is not None:
            slow_runner = slow_runner.next

            fast_runner = fast_runner.next
            fast_runner = fast_runner.next

        return slow_runner
