class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_list = list()

    def push(self, x: int) -> None:
        if not self.stack_list:
            self.stack_list.append((x, 0))

        else:
            if x <= self.stack_list[self.stack_list[-1][1]][0]:
                self.stack_list.append((x, len(self.stack_list)))
            else:
                self.stack_list.append((x, self.stack_list[-1][1]))

    def pop(self) -> None:
        self.stack_list.pop()

    def top(self) -> int:
        if not self.stack_list:
            return None

        return self.stack_list[-1][0]

    def getMin(self) -> int:
        return self.stack_list[self.stack_list[-1][1]][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
