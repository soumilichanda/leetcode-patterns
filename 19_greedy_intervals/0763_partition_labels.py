"""
LeetCode 763: Partition Labels
Difficulty: Medium
Pattern: Cluster 19 — Greedy Window Expansion

Invariant:
    Map each character to its rightmost index in the string.
    Traverse s: extend partition boundary to max(boundary, last_seen[char]).
    When index reaches boundary, record partition size and start next partition.

Time Complexity: O(n) — Two linear passes
Space Complexity: O(1) — Bounded alphabet map size <= 26
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {char: i for i, char in enumerate(s)}
        partitions = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last_idx[char])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1

        return partitions


if __name__ == "__main__":
    sol = Solution()
    assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert sol.partitionLabels("eccbbbbdec") == [10]
    print("LC 763 tests passed successfully!")
