"""
LeetCode 56: Merge Intervals
Pattern: Interval Sorting & Dynamic Interval Merging
Time Complexity: O(N log N)
Space Complexity: O(N) auxiliary space for sorted output
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals primarily by start time
        intervals.sort(key=lambda x: x[0])
        merged: List[List[int]] = [intervals[0]]

        for current in intervals[1:]:
            last_start, last_end = merged[-1]
            curr_start, curr_end = current

            if curr_start <= last_end:
                # Overlap detected: extend the existing interval horizon
                merged[-1][1] = max(last_end, curr_end)
            else:
                # Disjoint: start a new interval chain
                merged.append(current)

        return merged
