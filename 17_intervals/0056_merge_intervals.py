"""
LeetCode 56: Merge Intervals
Difficulty: Medium
Pattern: Interval Merging via Start-Time Sorting

Time Complexity: O(n log n) due to initial sort
Space Complexity: O(n) for sorted output array
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged: List[List[int]] = [intervals[0]]

        for current in intervals[1:]:
            prev = merged[-1]
            if current[0] <= prev[1]:
                prev[1] = max(prev[1], current[1])
            else:
                merged.append(current)

        return merged


if __name__ == "__main__":
    sol = Solution()
    test_data = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("LC 56 Merged:", sol.merge(test_data))
