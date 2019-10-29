class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = list()

        for ch in S:
            if ch == ")" and S[-1] == "(":
                stack.pop(-1)

            else:
                stack.append(ch)

        return len(stack)
