class Solution:

    def __init__(self):
        self.total_trees = 0
        self.mem_table_total_trees = dict()

    def num_trees_root(self, n, i):
        if len(n) == 0:
            return 1

        if i == len(n) - 1:
            return 1 * self.num_trees_root(n[:-1], 0)

        if i == 0:
            return 1 * self.num_trees_root(n[1:], 0)

        if (tuple(n), i) in self.mem_table_total_trees.keys():
            return self.mem_table_total_trees[(tuple(n), i)]

        self.mem_table_total_trees[(tuple(n), i)] = self.num_trees_root(n[:i], 0) * self.num_trees_root(n[i+1:], 0)

    def numTrees(self, n):
        total_trees = 0

        for i in range(len(n)):
            total_trees += self.num_trees_root(n, i)

        return total_trees
