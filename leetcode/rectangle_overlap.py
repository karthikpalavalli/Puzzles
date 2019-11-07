from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        length = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        width = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])

        print(length, width)

        if length > 0 and width > 0:
            return True

        return False


if __name__ == "__main__":
    sol = Solution()

    test_rec1 = [1, -4, 4, -1]
    test_rec2 = [2, -3, 3, -2]

    print(sol.isRectangleOverlap(test_rec1, test_rec2))