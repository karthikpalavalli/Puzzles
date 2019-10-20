from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for idx in range(len(s)//2):
            end_idx = len(s) - 1 - idx

            temp = s[idx]
            s[idx] = s[end_idx]
            s[end_idx] = temp


if __name__ == "__main__":
    test_str = ["h","e","l","l"]
    sol = Solution()
    sol.reverseString(test_str)
    print(test_str)