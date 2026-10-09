"""
LeetCode 973: K Closest Points to Origin
Difficulty: Medium
Pattern: Cluster 9 — Heaps & Priority Queues (Max-Heap via Negation)

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max-heap tracking k smallest Euclidean distances via negative distance
        max_heap: List[tuple[int, int, int]] = []

        for x, y in points:
            dist_sq = -(x * x + y * y)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist_sq, x, y))
            else:
                heapq.heappushpop(max_heap, (dist_sq, x, y))

        return [[x, y] for (_, x, y) in max_heap]


if __name__ == "__main__":
    sol = Solution()
    t1 = sol.kClosest([[1, 3], [-2, 2]], 1)
    assert t1 == [[-2, 2]], f"Expected [[-2, 2]], got {t1}"

    t2 = sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert len(t2) == 2

    print("LC 973: Verified successfully with max-heap O(n log k)")
