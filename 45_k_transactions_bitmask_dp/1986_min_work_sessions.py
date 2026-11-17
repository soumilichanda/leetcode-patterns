"""
LeetCode 1986: Minimum Number of Work Sessions to Finish the Tasks
Difficulty: Medium
Pattern: Cluster 45 — Dynamic Programming (Subset Bitmask State Compression)

Time Complexity: O(n * 2^n)
Space Complexity: O(2^n)
"""

from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        full_mask = (1 << n) - 1
        # dp[mask] = (min_sessions_count, min_remaining_capacity_used_in_current_session)
        inf_state = (n + 1, sessionTime + 1)
        dp = [inf_state] * (1 << n)
        dp[0] = (1, 0)

        for mask in range(1 << n):
            sessions, current_load = dp[mask]
            if sessions > n:
                continue

            for i in range(n):
                if mask & (1 << i):
                    continue
                next_mask = mask | (1 << i)
                task = tasks[i]

                if current_load + task <= sessionTime:
                    candidate = (sessions, current_load + task)
                else:
                    candidate = (sessions + 1, task)

                if candidate < dp[next_mask]:
                    dp[next_mask] = candidate

        return dp[full_mask][0]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minSessions([1, 2, 3], 3) == 2
    assert sol.minSessions([3, 1, 3, 1, 1], 8) == 2
    assert sol.minSessions([1, 2, 3, 4, 5], 15) == 1
    print("LC 1986 verified successfully!")
