"""
LeetCode 295: Find Median from Data Stream
Difficulty: Hard
Pattern: Cluster 21 — Dual Balanced Heaps (Max-Heap & Min-Heap)

Time Complexity:
    - addNum: O(log n)
    - findMedian: O(1)
Space Complexity: O(n)
"""

import heapq


class MedianFinder:
    def __init__(self):
        # small: max-heap (values negated) stores the smaller half
        # large: min-heap stores the larger half
        self.small: list[int] = []
        self.large: list[int] = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to max-heap (small)
        heapq.heappush(self.small, -num)

        # Step 2: Ensure max(small) <= min(large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance sizes (len(small) >= len(large) and difference <= 1)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5, f"Expected 1.5, got {mf.findMedian()}"
    mf.addNum(3)
    assert mf.findMedian() == 2.0, f"Expected 2.0, got {mf.findMedian()}"
    print("LC 295 verified successfully!")
