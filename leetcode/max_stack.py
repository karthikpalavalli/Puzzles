class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_list = list()

    def push(self, x: int) -> None:
        if not self.stack_list:
            self.stack_list.append((x, 0))

        else:
            if x >= self.stack_list[self.stack_list[-1][1]][0]:
                self.stack_list.append((x, len(self.stack_list)))
            else:
                self.stack_list.append((x, self.stack_list[-1][1]))

    def pop(self) -> None:
        return self.stack_list.pop()[0]

    def top(self) -> int:
        return self.stack_list[-1][0]

    def peekMax(self) -> int:
        return self.stack_list[self.stack_list[-1][1]][0]

    def popMax(self) -> int:
        max_index = self.stack_list[-1][1]
        val_at_max_index = self.stack_list[max_index][0]

        self.stack_list = self.stack_list[:max_index]

        if max_index < len(self.stack_list) - 1:
            temp_vals = [val[0] for val in self.stack_list[max_index + 1:]]
            for val in temp_vals:
                self.push(val)

        return val_at_max_index


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
