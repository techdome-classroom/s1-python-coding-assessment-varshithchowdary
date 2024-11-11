class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        r, c = len(grid), len(grid[0])
        seen = set()
        ans = 0

        def help(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if (x, y) in seen or grid[x][y] == 'W':
                    continue
                seen.add((x, y))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 'L':
                        stack.append((nx, ny))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'L' and (i, j) not in seen:
                    help(i, j)
                    ans += 1
                    
        return ans
