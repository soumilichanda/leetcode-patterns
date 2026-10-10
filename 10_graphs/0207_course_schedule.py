"""
LeetCode 207: Course Schedule
Difficulty: Medium
Pattern: Cluster 10 — Graphs (Topological Sort / Kahn's Algorithm)

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        in_degree: List[int] = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        queue: deque[int] = deque([i for i in range(numCourses) if in_degree[i] == 0])
        processed = 0

        while queue:
            curr = queue.popleft()
            processed += 1
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return processed == numCourses


if __name__ == "__main__":
    sol = Solution()
    assert sol.canFinish(2, [[1, 0]]) is True
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False
    print("LC 207 (Course Schedule): Verified successfully with Kahn's algorithm")
