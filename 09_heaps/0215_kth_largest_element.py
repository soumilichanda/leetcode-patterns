"""
LeetCode 215: Kth Largest Element in an Array
Difficulty: Medium
Pattern: Cluster 9 — Heaps & Priority Queues (Bounded Min-Heap)

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap: List[int] = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


if __name__ == "__main__":
    sol = Solution()
    t1 = sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    assert t1 == 5, f"Expected 5, got {t1}"

    t2 = sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    assert t2 == 4, f"Expected 4, got {t2}"

    print("LC 215: Verified successfully with bounded min-heap O(n log k)")
