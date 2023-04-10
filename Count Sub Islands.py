class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols, count = len(grid1), len(grid1[0]), 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid2[i][j] != 1:
                return

            grid2[i][j] = 0
            for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                dfs(i + x, j + y)

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    count += 1

        return count