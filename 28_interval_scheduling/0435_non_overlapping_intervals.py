"""
LeetCode 435: Non-overlapping Intervals
Pattern: Greedy Interval Scheduling (Earliest Deadline First)
Time Complexity: O(N log N)
Space Complexity: O(1) auxiliary space (ignoring sort stack)
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Greedy choice property: sort by finish time to leave maximum room for future intervals
        intervals.sort(key=lambda x: x[1])

        removals = 0
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            if curr_start < last_end:
                # Conflict: drop the interval that ends later to preserve future availability
                removals += 1
            else:
                # Non-overlapping: update active boundary
                last_end = curr_end

        return removals
