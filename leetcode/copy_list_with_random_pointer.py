# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.seen_nodes = dict()

    def copyRandomList(self, head):
        if self.seen_nodes[head]:
            return self.seen_nodes[head]

        node = Node(head.val, None, None)

        self.seen_nodes[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
