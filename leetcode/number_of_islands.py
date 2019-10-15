from typing import List


class Solution:
    def __init__(self):
        # self.visited_nodes = list()
        self.count_islands = 0

    def bfs(self, i, j, grid):
        queue = list()
        queue.append((i, j))

        self.count_islands += 1

        while queue:
            x_cord, y_cord = queue[0]
            queue = queue[1:]

            if x_cord > 0 and grid[x_cord - 1][y_cord] == '1':
                queue.append((x_cord - 1, y_cord))
                grid[x_cord - 1][y_cord] = '0'

            if x_cord < len(grid) - 1 and grid[x_cord + 1][y_cord] == '1':
                queue.append((x_cord + 1, y_cord))
                grid[x_cord + 1][y_cord] = '0'

            if y_cord > 0 and grid[x_cord][y_cord - 1] == '1':
                queue.append((x_cord, y_cord - 1))
                grid[x_cord][y_cord - 1] = '0'

            if y_cord < len(grid[0]) - 1 and grid[x_cord][y_cord + 1] == '1':
                queue.append((x_cord, y_cord + 1))
                grid[x_cord][y_cord + 1] = '0'

    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(i, j, grid)

        return self.count_islands
