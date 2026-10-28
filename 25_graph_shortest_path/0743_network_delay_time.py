"""
LeetCode 743: Network Delay Time
Difficulty: Medium
Pattern: Dijkstra's Algorithm (Min-Heap Priority Queue)

Time Complexity: O((V + E) log V)
Space Complexity: O(V + E)
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # min-heap priority queue storing (accumulated_dist, node)
        min_heap = [(0, k)]
        dist = {}

        while min_heap:
            d, u = heapq.heappop(min_heap)

            if u in dist:
                continue
            dist[u] = d

            for v, weight in graph[u]:
                if v not in dist:
                    heapq.heappush(min_heap, (d + weight, v))

        return max(dist.values()) if len(dist) == n else -1


if __name__ == "__main__":
    sol = Solution()
    # Test Case 1: Standard reachable DAG
    res1 = sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
    assert res1 == 2, f"Expected 2, got {res1}"

    # Test Case 2: Disconnected node
    res2 = sol.networkDelayTime([[1, 2, 1]], 2, 2)
    assert res2 == -1, f"Expected -1, got {res2}"

    print("LC 743 (Network Delay Time) tests passed successfully!")
