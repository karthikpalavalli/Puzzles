class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        max_length = 0
        length = 0

        for i in range(len(tree)):
            seen_trees = set()
            seen_trees.add(tree[i])
            length = 1

            for j in range(i+1, len(tree)):

                if tree[j] not in seen_trees and len(set(seen_trees)) == 2:
                    break

                else:
                    length += 1
                    seen_trees.add(tree[j])

            if length >= max_length:
                max_length = length

        if length >= max_length:
            max_length = length

        return max_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit([0] * 3200))
