"""
LeetCode 207: Course Schedule
Difficulty: Medium
Pattern: Cluster 23 — Graph BFS / DAG (Kahn's Topological Sort via In-Degree Queue)

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
        processed_count = 0

        while queue:
            curr = queue.popleft()
            processed_count += 1
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Invariant: If processed == V, graph is a DAG (zero directed cycles)
        return processed_count == numCourses


if __name__ == "__main__":
    sol = Solution()
    assert sol.canFinish(2, [[1, 0]]) is True
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False
    assert sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    print("LC 207 (Course Schedule): All topological Kahn assertions passed!")
