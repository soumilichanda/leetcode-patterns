"""
LeetCode 452: Minimum Number of Arrows to Burst Balloons
Pattern: Greedy Interval Intersection / Earliest End Coordinate
Time Complexity: O(N log N)
Space Complexity: O(1) auxiliary space (ignoring Timsort space)
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Greedily sort balloons by end coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points[1:]:
            # If current balloon starts after the current arrow position, fire a new arrow
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows
