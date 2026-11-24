"""
LeetCode 1857: Largest Color Value in a Directed Graph
Difficulty: Hard
Pattern: Cluster 52 — Dynamic Programming (Topological Sort Frequency Propagation + Cycle Detection)

Time Complexity: O(26 * (V + E))
Space Complexity: O(26 * V)
"""

from collections import deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj: List[List[int]] = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        dp = [[0] * 26 for _ in range(n)]
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                dp[i][ord(colors[i]) - 97] = 1
                queue.append(i)

        visited = 0
        ans = 0

        while queue:
            u = queue.popleft()
            visited += 1
            ans = max(ans, max(dp[u]))

            for v in adj[u]:
                v_color = ord(colors[v]) - 97
                for c in range(26):
                    candidate = dp[u][c] + (1 if c == v_color else 0)
                    if candidate > dp[v][c]:
                        dp[v][c] = candidate
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return ans if visited == n else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3
    assert sol.largestPathValue("a", [[0, 0]]) == -1
    print("LC 1857 verified successfully!")
