"""
LeetCode 57: Insert Interval
Difficulty: Medium
Pattern: Three-Phase Greedy Interval Partitioning

Time Complexity: O(N) single-pass scan
Space Complexity: O(1) auxiliary space (O(N) output storage)
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        merged: List[List[int]] = []
        i = 0
        n = len(intervals)

        # Phase 1: Append all intervals ending strictly before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Phase 2: Merge overlapping intervals by expanding bounds
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        merged.append(newInterval)

        # Phase 3: Append all remaining intervals starting after merged window
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged


if __name__ == "__main__":
    sol = Solution()
    res1 = sol.insert([[1, 3], [6, 9]], [2, 5])
    assert res1 == [[1, 5], [6, 9]], f"Expected [[1, 5], [6, 9]], got {res1}"

    res2 = sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    assert res2 == [[1, 2], [3, 10], [12, 16]], f"Expected [[1, 2], [3, 10], [12, 16]], got {res2}"
    print("LC 57 Insert Interval verified successfully!")
