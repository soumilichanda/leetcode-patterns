"""
LeetCode 200: Number of Islands
Difficulty: Medium
Pattern: Cluster 10 — Graphs (2D Grid BFS Connected Components)

Time Complexity: O(m * n)
Space Complexity: O(min(m, n)) for BFS queue
"""

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            grid[r][c] = "0"  # Sink island in-place

            while queue:
                row, col = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    bfs(r, c)

        return island_count


if __name__ == "__main__":
    sol = Solution()
    test_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    result = sol.numIslands(test_grid)
    assert result == 3, f"Expected 3 islands, got {result}"
    print(f"LC 200 (Number of Islands): Verified successfully with count = {result}")
