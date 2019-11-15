class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = list()
        self.pop_stack = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)

    def transfer_elements(self):
        self.pop_stack = reversed(self.push_stack)
        self.push_stack = list()

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.pop_stack:
            return self.pop_stack.pop(0)

        self.transfer_elements()

        return self.pop_stack.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.pop_stack:
            return self.pop_stack[0]

        self.transfer_elements()

        return self.pop_stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.push_stack and not self.pop_stack:
            return True

        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
