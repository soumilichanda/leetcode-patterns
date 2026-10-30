"""
LeetCode 253: Meeting Rooms II
Difficulty: Medium
Pattern: Chronological Sweep-Line / Min-Heap Room Allocation

Time Complexity: O(N log N) where N is number of intervals
Space Complexity: O(N) auxiliary space for min-heap
"""

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Invariant 1: Sort chronologically by meeting start times
        intervals.sort(key=lambda x: x[0])

        # Invariant 2: Min-heap tracks earliest end time among active rooms
        rooms: List[int] = []
        heapq.heappush(rooms, intervals[0][1])

        for start, end in intervals[1:]:
            # If the earliest finishing room is free before this meeting starts, reuse it
            if rooms[0] <= start:
                heapq.heapreplace(rooms, end)
            else:
                heapq.heappush(rooms, end)

        return len(rooms)


if __name__ == "__main__":
    sol = Solution()
    case1 = [[0, 30], [5, 10], [15, 20]]
    assert sol.minMeetingRooms(case1) == 2, f"Expected 2, got {sol.minMeetingRooms(case1)}"
    case2 = [[7, 10], [2, 4]]
    assert sol.minMeetingRooms(case2) == 1, f"Expected 1, got {sol.minMeetingRooms(case2)}"
    print("LC 253 Meeting Rooms II verified successfully!")
