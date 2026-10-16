"""
LeetCode 57: Insert Interval
Difficulty: Medium
Pattern: Disjoint Interval Merging (3-Stage Linear Partition)

Time Complexity: O(n) single pass
Space Complexity: O(n) auxiliary result array
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        i = 0
        n = len(intervals)

        # 1. Chunks fully before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. Overlapping chunks: expand newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 3. Chunks fully after newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print("LC 57 Insert:", sol.insert([[1, 3], [6, 9]], [2, 5]))
