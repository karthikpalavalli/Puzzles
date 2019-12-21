import collections


class Solution(object):
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, d+1))

        if any(0 in row for row in grid):
            return 0

        return d


if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,0], [0,0,0], [0,0,0]]

    grid = [[]]

    print(sol.orangesRotting(grid))
