class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        N = len(grid)
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        q = deque([(0, 0)])
        visited = set([(0, 0)])

        def get_neighbours(row, col):
            for x_offset, y_offset in offsets:
                new_row, new_col = row + x_offset, col + y_offset
                if 0 <= new_row < N and 0 <= new_col < N and grid[new_row][new_col] == 0 and (
                new_row, new_col) not in visited:
                    yield (new_row, new_col)

        current_distance = 1

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                if row == N - 1 and col == N - 1:
                    return current_distance

                for p in get_neighbours(row, col):
                    visited.add(p)
                    q.append(p)

            current_distance += 1

        return -1