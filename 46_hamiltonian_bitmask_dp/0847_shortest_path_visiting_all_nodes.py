"""
LeetCode 847: Shortest Path Visiting All Nodes
Difficulty: Hard
Pattern: Cluster 46 — Hamiltonian Path / BFS over Bitmask State Space

Time Complexity: O(n^2 * 2^n)
Space Complexity: O(n * 2^n)
"""

from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n <= 1:
            return 0

        target_mask = (1 << n) - 1
        queue = deque((i, 1 << i, 0) for i in range(n))
        visited = {(i, 1 << i) for i in range(n)}

        while queue:
            node, mask, dist = queue.popleft()
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                if next_mask == target_mask:
                    return dist + 1
                state = (neighbor, next_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, next_mask, dist + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.shortestPathLength([[1, 2, 3], [0], [0], [0]]) == 4
    assert sol.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]) == 4
    print("LC 847 verified successfully!")
