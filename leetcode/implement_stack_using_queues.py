class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_one = list()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue_one.append(x)

        # Bubble up operation
        for idx in range(len(self.queue_one) - 1, 0, -1):
            current_element = self.queue_one[idx - 1]
            self.queue_one[idx - 1] = self.queue_one[idx]
            self.queue_one[idx] = current_element

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue_one.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue_one[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.queue_one:
            return True

        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()