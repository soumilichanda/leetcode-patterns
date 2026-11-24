"""
LeetCode 329: Longest Increasing Path in a Matrix
Difficulty: Hard
Pattern: Cluster 52 — Dynamic Programming (DAG Out-Degree Topological Peeling)

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from collections import deque
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        out_degree = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                val = matrix[r][c]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > val:
                        out_degree[r][c] += 1

        queue = deque(
            (r, c)
            for r in range(rows)
            for c in range(cols)
            if out_degree[r][c] == 0
        )

        layers = 0
        while queue:
            layers += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                val = matrix[r][c]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < val:
                        out_degree[nr][nc] -= 1
                        if out_degree[nr][nc] == 0:
                            queue.append((nr, nc))

        return layers


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert sol.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert sol.longestIncreasingPath([[1]]) == 1
    print("LC 329 verified successfully!")
