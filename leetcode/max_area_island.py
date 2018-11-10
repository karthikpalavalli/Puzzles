class Solution:
    def check_visited(self, indices_to_add, visited):
        queue = list()

        for index in indices_to_add:
            if index not in visited:
                queue.append(index)
                visited.append(index)

        return queue, visited

    def search_connected_components(self, i, j, visited, grid):
        indices_to_add = list()

        row_len = len(grid)
        col_len = len(grid[0])

        if i > 0 and grid[i-1][j] == 1:
            indices_to_add.append((i-1, j))

        if j > 0 and grid[i][j-1] == 1:
            indices_to_add.append((i, j-1))

        if i != row_len - 1 and grid[i+1][j] == 1:
            indices_to_add.append((i+1, j))

        if j != col_len - 1 and grid[i][j+1] == 1:
            indices_to_add.append((i, j+1))

        queue, visited = self.check_visited(indices_to_add, visited)

        return queue, visited

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row_len = len(grid)
        col_len = len(grid[0])
        max_connected = 0

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    visited_components = list()
                    queue = list()

                    visited_components.append((i, j))
                    queue.append((i, j))

                    while queue:
                        new_i, new_j = queue[0][0], queue[0][1]
                        queue.pop(0)

                        curr_queue, curr_visited = self.search_connected_components(new_i, new_j,
                                                                                    visited_components,
                                                                                    grid)

                        visited_components += curr_visited
                        queue += curr_queue

                    if len(visited_components) > max_connected:
                        max_connected = len(visited_components)

        return max_connected
