"""
LeetCode 435: Non-overlapping Intervals
Difficulty: Medium
Pattern: Cluster 19 — Greedy Scheduling (Interval Elimination via End-Time Sort)

Invariant:
    Sort intervals primarily by end coordinate. Whenever the current interval's
    start < prev_end, an overlap occurs; greedily discard the one ending later
    (which is the current one, keeping prev_end minimal).

Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary (or O(n) for sort space)
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort by end time
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # Overlap detected: drop this interval
                removals += 1
            else:
                # Non-overlapping: update boundary
                prev_end = end

        return removals


if __name__ == "__main__":
    sol = Solution()
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    print("LC 435 tests passed successfully!")
