class Solution:
    def dfs(self, r, c, base_r, base_c, grid, rows, cols, visited, shape):
        visited[r][c] = 1
        shape.append((r-base_r, c-base_c))

        for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
            new_x, new_y = r+x, c+y

            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                continue

            if visited[new_x][new_y] == 1:
                continue

            if grid[new_x][new_y] == 0:
                continue

            self.dfs(new_x, new_y, base_r, base_c, grid, rows, cols, visited, shape)

    def numberisland(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        uniqueisland = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    shape = []

                    self.dfs(r, c, r, c, grid, rows, cols, visited, shape)

                    uniqueisland.add(tuple(shape))

        return len(uniqueisland)


grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

obj = Solution()
result = obj.numberisland(grid)

print("Number of distinct islands:", result)