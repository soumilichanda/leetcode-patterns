"""
LeetCode 739: Daily Temperatures
Difficulty: Medium
Pattern: Monotonic Decreasing Stack (Index Tracking)

Time Complexity: O(n) amortized
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stores indices in monotonic decreasing temperature order

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)

        return result


if __name__ == "__main__":
    sol = Solution()
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    res = sol.dailyTemperatures(temps)
    print("=== LC 739: Daily Temperatures Verification ===")
    print(f"Input:    {temps}")
    print(f"Output:   {res}")
    print(f"Expected: [1, 1, 4, 2, 1, 1, 0, 0]")